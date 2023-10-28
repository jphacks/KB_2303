import os
import sys

from fastapi import Request, APIRouter, HTTPException
from enum import Enum
from crud.line_communication_state import LineCommunicationStateCrud
from crud.schemas import LINECommunicationStateSchema

from linebot.v3.webhook import WebhookParser
from linebot.v3.messaging import (
    AsyncApiClient,
    AsyncMessagingApi,
    Configuration,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
from linebot.models import (
    TextSendMessage
)


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
def set_data(line_id: str, state: str, data: dict):
    with LineCommunicationStateCrud() as line_communication_state_crud:
        line_communication_state_crud.set(
            line_id,
            LINECommunicationStateSchema(state=state, data=data)
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
    START = 10201  # ユーザの登録処理開始
    GROUP_JOIN_SUCCESS = 10501  # グループへの参加が完了した状態
    NAME_SUCCESS = 10601  # 氏名の登録が完了した状態
    CHARACTER_CHOICE_SUCCESS = 10701  # キャラクター選択が完了した状態
    GOAL_SUCCESS = 10801  # 目標の設定が完了した状態
    INTERVAL_SUCCESS = 10901  # インターバルの設定が成功した時
    INTERVAL_FAIL = 10902  # インターバルの設定が失敗した時
    TARGET_SUCCESS = 11001  # 短期目標の設定が完了した時

    # 現状使っていないもの
    NO_PROCESS = 10101  # 登録処理が走っていない状態
    ID_SUCCESS = 10301  # ユーザIDの登録がされた状態
    GROUP_SEARCH_SUCCESS = 10401  # 正しいグループIDが入力された時
    GROUP_SEARCH_FAIL = 10402  # 誤ったグループIDが入力された時


@router.post("/callback")
async def handle_callback(request: Request):
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = await request.body()
    body = body.decode()

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    for ev in events:
        if not isinstance(ev, MessageEvent):
            continue
        if not isinstance(ev.message, TextMessageContent):
            continue
        line_id = ev.source.user_id

        # 何もしていないとき
        if get_status(line_id) == None:
            if ev.message.text == "はじめる":
                set_data(line_id, "START", {"line_id": line_id})
                return "GroupIDを聞く"
            else:
                return "回答, はじめると送ってね"
        
        # GroupIDを聞く
        elif get_status(line_id) == "START":
            # 正しいグループIDかどうか
            if ev.message.text == True:
                return "GroupNameに参加しますか？" # カルーセルで
            # グループに参加
            elif ev.message.text == "参加する":
                set_data(line_id, "GROUP_JOIN_SUCCESS", {"group_id": group_id})
                return "GroupNameに参加しました!, 次にあなたの名前を教えてください"
            # 誤ったグループIDの場合
            else:
                return "回答, グループIDが間違っているようです。もう一度正しいものを送ってください。"
        # 氏名を聞く
        elif get_status(line_id) == "GROUP_JOIN_SUCCESS":
            if ev.message.text == 
            






















        reply_message_list = []

        if get_status(line_id):
            ev.message.text == "はじめる":
            
            reply_message_list.append(TextMessage(
                text="GroupIDがあれば入力してください。\nなければなしと送信してください。"))

        # ユーザが未登録andはじめると送られていない
        if True:
            await line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=ev.reply_token,
                    messages=[
                        TextMessage(text="はじめると送ってください(else)"),
                    ]
                )
            )

        await line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=ev.reply_token,
                messages=reply_message_list
            )
        )
        return 'OK'

    return 'OK'
