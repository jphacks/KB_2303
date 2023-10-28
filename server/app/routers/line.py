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
    ReplyMessageRequest
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


# line_idに紐づくデータを取得
def get_data(line_id: str):
    with LineCommunicationStateCrud() as line_communication_state_crud:
        data = line_communication_state_crud.get(line_id)
    return data.data


# 処理状況
def get_status(line_id: str):
    # lineのidから処理状況のEnumの値を返して欲しい
    with LineCommunicationStateCrud() as line_communication_state_crud:
        registration_status = line_communication_state_crud.get(line_id)

    return registration_status.state


# line_idに紐づくデータを登録、ステータスの更新
def set_saved_data(line_id: str, schema: LINECommunicationStateSchema):
    with LineCommunicationStateCrud() as line_communication_state_crud:
        line_communication_state_crud.set(
            line_id,
            schema
        )


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
    INPUT_NAME = 10201  # 氏名を聞く
    INPUT_GOAL = 10301  # 目標を聞く
    INPUT_INTERVAL = 10401  # メンタリングの頻度を聞く
    INPUT_TARGET = 10501  # 短期目標を聞く
    CONFIRM_REGISTRATION = 10601  # 登録内容を確認
    CONFIRM_RETURN_TO_INPUT_NAME = 10602  # 氏名の入力に戻るか確認


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

        # stateを確認する
        saved_data: LINECommunicationStateSchema | None = get_saved_data(line_id)

        # 送信メッセージのリスト
        reply_message_list = []

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
                reply_message_list.append(TextMessage(
                    text=f"グループ「{group.name}」に参加しますか？")
                )
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
                    text="氏名を入力してください")
                )
                # 状態を更新
                saved_data.state = STATUS.INPUT_NAME.name
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

        # テスト
        reply_message_list.append(TextMessage(
            text=f"入力: {input_text}, ステータス: {saved_status.name}, データ: {saved_data.data}"
        ))

        # reply_message_listを送信
        await line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=ev.reply_token,
                messages=reply_message_list
            )
        )
