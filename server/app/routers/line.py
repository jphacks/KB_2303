import os
import sys

from fastapi import Request, APIRouter, HTTPException
from enum import Enum, auto

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
    TextMessageContent,
    UserSource
)
from linebot.models import (
    TextSendMessage
)

# TODO
# ユーザの情報を取得


def get_user(line_id: str):
    # id,名前,グループid
    return {"id": "0",
            "name": "test",
            "group_id": "0"
            }

# TODO
# ユーザの詳細情報を取得


def get_user_config(user_id: str):
    # userConfigからそれぞれ取得
    return {"character_id": "0",
            "intervel": "0",
            "goal": "something goal text"
            }

# TODO
# ユーザ情報の登録状況


def get_config_registration_status(line_id: str):
    # lineのidからユーザの登録状況のEnumの値を返して欲しい
    return CONFIG_REGISTRATION_STATUS.NO_PROCESS


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


class CONFIG_REGISTRATION_STATUS(Enum):
    NO_PROCESS = auto()  # ユーザの登録処理が走っていない状態
    START = auto()  # ユーザの登録処理開始
    ID_SUCCESS = auto()  # ユーザIDの登録がされた状態
    GROUP_SEARCH_SUCCESS = auto()  # 正しいグループIDが入力された時
    GROUP_SEARCH_FAIL = auto()  # 誤ったグループIDが入力された時
    GROUP_JOIN_SUCCESS = auto()  # グループへの参加が完了した状態
    CHARACTER_CHOICE_SUCCESS = auto()  # キャラクター選択が完了した状態
    NAME_SUCCESS = auto()  # 氏名の登録が完了した状態
    GOAL_SUCCESS = auto()  # 目標の設定が完了した状態
    INTERVAL_SUCCESS = auto()  # インターバルの設定が成功した時
    INTERVAL_FAIL = auto()  # インターバルの設定が失敗した時
    TARGET_SUCCESS = auto()  # 短期目標の設定が完了した時


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
        # ユーザの登録情報を取得(どこまで入力中か)
        user_info = get_user(line_id)
        reply_message_list = []

        status = get_config_registration_status()
        if ev.message.text == "はじめる":
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
