import os
import sys
from enum import Enum

from fastapi import Request, APIRouter, HTTPException, Depends
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    AsyncApiClient,
    AsyncMessagingApi,
    Configuration,
    TextMessage,
    ReplyMessageRequest,
    TemplateMessage, ButtonsTemplate, MessageAction
)
from linebot.v3.webhook import WebhookParser
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    UserSource
)

from crud.line_communication_state import LineCommunicationStateCrud
from crud.schemas import LINECommunicationStateSchema
from db.crud.group import get_by_user_invite_token
from db.session import get_db


# redisに保存されたデータを取得
def get_saved_data(line_id: str) -> LINECommunicationStateSchema | None:
    with LineCommunicationStateCrud() as line_communication_state_crud:
        data = line_communication_state_crud.get(line_id)
    return data


# line_idに紐づくデータを登録、ステータスの更新
def set_saved_data(line_id: str, schema: LINECommunicationStateSchema):
    with LineCommunicationStateCrud() as line_communication_state_crud:
        line_communication_state_crud.set(
            line_id,
            schema
        )


# ステータスを削除
def delete_saved_data(line_id: str):
    with LineCommunicationStateCrud() as line_communication_state_crud:
        line_communication_state_crud.delete(line_id)


# define router
router = APIRouter(
    tags=["LINEBot"],
    prefix="/line"
)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

configuration = Configuration(
    access_token=channel_access_token
)

async_api_client = AsyncApiClient(configuration)
line_bot_api = AsyncMessagingApi(async_api_client)
parser = WebhookParser(channel_secret)


# "10101" 上1桁：1-ユーザの登録,2-定期メンタリング 上23桁：処理順 上45桁：同処理で分岐する場合1ずつ加算する
class STATUS(Enum):
    # 1xxxx: ユーザの登録
    INPUT_GROUP_ID = 10101  # グループIDを聞く
    CONFIRM_GROUP_JOIN = 10102  # グループに参加するか確認
    SERECT_CHARACTER = 10201
    INPUT_NAME = 10301  # 氏名を聞く
    INPUT_GOAL = 10401  # 目標を聞く
    INPUT_INTERVAL = 10501  # メンタリングの頻度を聞く
    INPUT_TARGET = 10601  # 短期目標を聞く
    CONFIRM_REGISTRATION = 10701  # 登録内容を確認
    CONFIRM_RETURN_TO_INPUT_NAME = 10702  # 氏名の入力に戻るか確認


@router.post("/callback")
async def handle_callback(
        request: Request,
        db=Depends(get_db)
):
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = (await request.body()).decode()

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    for ev in events:
        if not isinstance(ev, MessageEvent):
            continue
        if not isinstance(ev.message, TextMessageContent):
            continue

        # event.sourceがuserでない場合は処理しない
        if ev.source.type != "user":
            continue

        # line_idを取得
        source: UserSource = ev.source
        line_id = source.user_id
        # textを取得
        input_text = ev.message.text.strip()

        # 送信メッセージのリスト
        reply_message_list = []

        # ----debug-----
        # TODO: けす

        if input_text == "clearstate":
            delete_saved_data(line_id)
            reply_message_list.append(TextMessage(
                text="ステータスを削除しました")
            )

        # stateを確認する
        saved_data: LINECommunicationStateSchema | None = get_saved_data(
            line_id)

        # ----end of debug-----

        # 初期状態である場合
        if saved_data is None:
            # はじめると送られているか
            if input_text == "はじめる":
                # GroupID入力へ移行
                reply_message_list.append(TextMessage(
                    text="管理者から発行されたGroupIDを入力してください")
                )
                # 状態を更新
                set_saved_data(line_id, LINECommunicationStateSchema(
                    state=STATUS.INPUT_GROUP_ID.name,
                    data={}
                ))

            else:
                reply_message_list.append(TextMessage(
                    text="「はじめる」と送ってください")
                )

        # 初期状態でない場合
        else:
            # 状態を取得
            saved_status: STATUS = STATUS[saved_data.state]

            # GroupIDを聞いた場合
            if saved_status == STATUS.INPUT_GROUP_ID:
                # グループIDからグループを取得
                group = get_by_user_invite_token(db, input_text)
                # グループが存在しない場合は再入力を求める
                if group is None:
                    reply_message_list.append(TextMessage(
                        text="グループIDが間違っているようです。もう一度正しいものを送ってください。")
                    )

                # グループが存在した場合、グループに参加するか確認する
                else:
                    reply_message_list.append(TemplateMessage(
                        alt_text=f"{group.name}に参加しますか？",
                        template=ButtonsTemplate(
                            text=f"{group.name}に参加しますか？",
                            actions=[
                                MessageAction(
                                    label="はい",
                                    text="はい"
                                ),
                                MessageAction(
                                    label="いいえ",
                                    text="いいえ"
                                )
                            ]
                        )
                    ))
                    # 状態を更新
                    saved_data.state = STATUS.CONFIRM_GROUP_JOIN.name
                    saved_data.data["group_id"] = group.id
                    set_saved_data(line_id, saved_data)

            # グループに参加するか確認していた場合
            elif saved_status == STATUS.CONFIRM_GROUP_JOIN:
                # 参加する場合
                if input_text == "はい":
                    # 氏名を聞く
                    reply_message_list.append(TextMessage(
                        text="キャラクターを選択してください")
                    )
                    # 状態を更新
                    saved_data.state = STATUS.SERECT_CHARACTER.name
                    set_saved_data(line_id, saved_data)

                # 参加しない場合
                elif input_text == "いいえ":
                    # 再入力を求める
                    reply_message_list.append(TextMessage(
                        text="参加をキャンセルしました、再度グループIDを入力してください")
                    )
                    # 状態を更新
                    saved_data.state = STATUS.INPUT_GROUP_ID.name
                    del saved_data.data["group_id"]
                    set_saved_data(line_id, saved_data)

                # どちらでもない場合
                else:
                    # グループに参加するか確認する
                    reply_message_list.append(TextMessage(
                        text="「はい」か「いいえ」でお答えください。")
                    )
            # キャラクターを選択していた場合
            elif saved_status == STATUS.SERECT_CHARACTER:
                if input_text == "":
                    reply_message_list.append(TextMessage(
                        text="キャラクターを選択してください"
                    ))
                else:
                    # 氏名を聞く
                    reply_message_list.append(TextMessage(
                        text="氏名を入力してください"
                    ))
                    # 状態を更新
                    saved_data.state = STATUS.INPUT_NAME.name
                    saved_data.data["character_id"] = input_text
                    set_saved_data(line_id, saved_data)

            # 氏名を聞いていた場合
            elif saved_status == STATUS.INPUT_NAME:
                if input_text == "":
                    reply_message_list.append(TextMessage(
                        text="氏名を入力してください")
                    )
                else:
                    # 目標を聞く
                    reply_message_list.append(TextMessage(
                        text="目標を入力してください")
                    )
                    # 状態を更新
                    saved_data.state = STATUS.INPUT_GOAL.name
                    saved_data.data["name"] = input_text
                    set_saved_data(line_id, saved_data)

            # 目標を聞いていた場合
            elif saved_status == STATUS.INPUT_GOAL:
                if input_text == "":
                    reply_message_list.append(TextMessage(
                        text="目標を入力してください")
                    )
                else:
                    # メンタリングの頻度を聞く
                    reply_message_list.append(TemplateMessage(
                        alt_text=f"メンタリングの頻度を選択してください",
                        template=ButtonsTemplate(
                            text=f"メンタリングの頻度を選択してください",
                            actions=[
                                MessageAction(
                                    label="毎日",
                                    text="1"
                                ),
                                MessageAction(
                                    label="3日に1回",
                                    text="3"
                                ),
                                MessageAction(
                                    label="週に1回",
                                    text="7"
                                )
                            ]
                        )
                    ))
                    # 状態を更新
                    saved_data.state = STATUS.INPUT_INTERVAL.name
                    saved_data.data["goal"] = input_text
                    set_saved_data(line_id, saved_data)

            # メンタリングの頻度を聞いていた場合
            elif saved_status == STATUS.INPUT_INTERVAL:
                if input_text not in ["1", "3", "7"]:
                    reply_message_list.append(TextMessage(
                        text="上のボタンからメンタリングの頻度を選択してください")
                    )
                else:
                    # 短期目標を聞く
                    reply_message_list.append(TextMessage(
                        text=f"{input_text}日後までの短期目標を入力してください")
                    )
                    # 状態を更新
                    saved_data.state = STATUS.INPUT_TARGET.name
                    saved_data.data["interval_days"] = int(input_text)
                    set_saved_data(line_id, saved_data)

            # 短期目標を聞いていた場合
            elif saved_status == STATUS.INPUT_TARGET:
                if input_text == "":
                    reply_message_list.append(TextMessage(
                        text=f'{saved_data.data["interval_days"]}日後までの短期目標を入力してください')
                    )
                else:
                    # 状態を代入
                    saved_data.state = STATUS.CONFIRM_REGISTRATION.name
                    saved_data.data["target"] = input_text

                    # 登録内容を確認
                    reply_text = "\n".join([
                        f'氏名: {saved_data.data["name"]}',
                        f'目標: {saved_data.data["goal"]}',
                        f'メンタリングの頻度: {saved_data.data["interval_days"]}',
                        f'{saved_data.data["interval_days"]}日後までの目標: {saved_data.data["target"]}'
                    ])
                    reply_message_list.append(TemplateMessage(
                        alt_text=f"下記の内容でよろしいですか？\n{reply_text}",
                        template=ButtonsTemplate(
                            text=f"下記の内容でよろしいですか？\n{reply_text}",
                            actions=[
                                MessageAction(
                                    label="確定する",
                                    text="確定する"
                                ),
                                MessageAction(
                                    label="修正する",
                                    text="修正する"
                                )
                            ]
                        )
                    ))
                    # 状態を更新
                    set_saved_data(line_id, saved_data)

            # 登録内容の確認をしていた場合
            elif saved_status == STATUS.CONFIRM_REGISTRATION:
                if input_text == "確定する":
                    # TODO: DBに登録して!!!!

                    # cacheを削除
                    delete_saved_data(line_id)
                    reply_message_list.append(TextMessage(
                        text="登録が完了しました")
                    )
                elif input_text == "修正する":
                    # 氏名の入力に戻るか確認
                    reply_message_list.append(TemplateMessage(
                        alt_text=f"氏名の入力にもどりますが、本当によろしいですか？",
                        template=ButtonsTemplate(
                            text=f"氏名の入力にもどりますが、本当によろしいですか？",
                            actions=[
                                MessageAction(
                                    label="やり直す",
                                    text="やり直す"
                                ),
                                MessageAction(
                                    label="確認にもどる",
                                    text="確認にもどる"
                                )
                            ]
                        )
                    ))
                    # 状態を更新
                    saved_data.state = STATUS.CONFIRM_RETURN_TO_INPUT_NAME.name
                    set_saved_data(line_id, saved_data)
                else:
                    reply_message_list.append(TextMessage(
                        text="上のボタンから選択してください")
                    )

            # 氏名の入力に戻るか確認をしていた場合
            elif saved_status == STATUS.CONFIRM_RETURN_TO_INPUT_NAME:
                if input_text == "やり直す":
                    # 氏名を聞く
                    reply_message_list.append(TextMessage(
                        text="氏名を入力してください"
                    ))
                    # 状態を更新
                    saved_data.state = STATUS.INPUT_NAME.name
                    set_saved_data(line_id, saved_data)
                elif input_text == "確認にもどる":
                    # 状態を代入
                    saved_data.state = STATUS.CONFIRM_REGISTRATION.name

                    # 登録内容を確認
                    reply_text = "\n".join([
                        f'氏名: {saved_data.data["name"]}',
                        f'目標: {saved_data.data["goal"]}',
                        f'メンタリングの頻度: {saved_data.data["interval_days"]}',
                        f'{saved_data.data["interval_days"]}日後までの目標: {saved_data.data["target"]}'
                    ])
                    reply_message_list.append(TemplateMessage(
                        alt_text=f"下記の内容でよろしいですか？\n{reply_text}",
                        template=ButtonsTemplate(
                            text=f"下記の内容でよろしいですか？\n{reply_text}",
                            actions=[
                                MessageAction(
                                    label="確定する",
                                    text="確定する"
                                ),
                                MessageAction(
                                    label="修正する",
                                    text="修正する"
                                )
                            ]
                        )
                    ))
                    # 状態を更新
                    set_saved_data(line_id, saved_data)
                else:
                    reply_message_list.append(TextMessage(
                        text="上のボタンから選択してください")
                    )

        # テスト
        reply_message_list.append(TextMessage(
            text=f"入力: {input_text}, ステータス: {saved_data.state if saved_data is not None else 'None'}, "
                 f"データ: {saved_data.data if saved_data is not None else 'None'}"
        ))

        # reply_message_listを送信
        await line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=ev.reply_token,
                messages=reply_message_list
            )
        )
