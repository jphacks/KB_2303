import os
import sys

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import Request, APIRouter, HTTPException, Depends
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    AsyncApiClient,
    ApiClient,
    AsyncMessagingApi,
    MessagingApi,
    Configuration,
    TextMessage,
    ReplyMessageRequest, PushMessageRequest, Sender
)
from linebot.v3.webhook import WebhookParser
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    UserSource
)

from crud.schemas import LINECommunicationStateSchema
from db.connection import SessionLocal
from db.crud import user as user_crud, report as report_crud
from db.session import get_db
from .controller.mentoring import mentoring_controller
from .controller.registration import registration_controller
from .data import MENTORS, MentorBase
from .model.state import STATUS
from .util.session import get_saved_data, delete_saved_data, set_saved_data

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
async_msg_api = AsyncMessagingApi(async_api_client)

api_client = ApiClient(configuration)
msg_api = MessagingApi(api_client)

parser = WebhookParser(channel_secret)


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

        # userを取得
        user = user_crud.get_by_line_id(db, line_id)

        # stateを確認する
        saved_data: LINECommunicationStateSchema | None = get_saved_data(line_id)

        # 送信するメッセージのリスト
        reply_message_list = []

        # ----debug-----
        # TODO: けす

        if input_text == "clearstate":
            delete_saved_data(line_id)
            saved_data = None
            reply_message_list.append(TextMessage(
                text="ステータスを削除しました")
            )

        if input_text == "getstate":
            reply_message_list.append(TextMessage(
                text=f"ステータスを取得しました\n{saved_data}")
            )

        # ----end of debug-----

        # 未登録ユーザ
        if user is None:
            # メンター取得
            if saved_data is None or "mentor_id" not in saved_data.data:
                mentor = MENTORS[0]
            else:
                mentor = MENTORS[saved_data.data["mentor_id"]]

            reply_message_list.extend(registration_controller(
                saved_data=saved_data,
                line_id=line_id,
                input_text=input_text,
                mentor=mentor,
                db=db
            ))

        # 登録済みユーザ
        else:
            # メンター取得
            mentor: MentorBase = MENTORS[user.config.mentor_id]

            if saved_data is None:
                # 通常の会話
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_INACTIVE
                ))
            else:
                # メンタリング会話
                reply_message_list.extend(mentoring_controller(
                    saved_data=saved_data,
                    line_id=line_id,
                    input_text=input_text,
                    mentor=mentor,
                    user=user,
                    db=db
                ))

        # reply_message_listの全てにsenderを設定
        sender = Sender(
            name=mentor.NAME
        )
        if mentor.ICON_PATH is not None:
            sender.icon_url = f"{mentor.IMG_DOMAIN}{mentor.ICON_PATH}"

        for reply_message in reply_message_list:
            reply_message.sender = sender

        # reply_message_listを送信
        await async_msg_api.reply_message(
            ReplyMessageRequest(
                reply_token=ev.reply_token,
                messages=reply_message_list,
            )
        )


def send_mentoring_start_messages():
    with SessionLocal() as db:
        reports = report_crud.get_need_to_process_scheduled_reports(db)

        for report in reports:
            user = report.user
            line_id = user.line_id
            config = user.config
            mentor = MENTORS[config.mentor_id]

            print(mentor.NAME)
            print(config.mentor_id)

            saved_data = get_saved_data(line_id)

            sender = Sender(
                name=mentor.NAME
            )
            if mentor.ICON_PATH is not None:
                sender.icon_url = f"{mentor.IMG_DOMAIN}{mentor.ICON_PATH}"

            if saved_data is None:
                msg_api.push_message(
                    PushMessageRequest(
                        to=line_id,
                        messages=[
                            TextMessage(
                                text=mentor.RESPONSE_PUSH_START,
                                sender=sender
                            ),
                            TextMessage(
                                text=mentor.RESPONSE_PUSH_HEARING,
                                sender=sender
                            )
                        ]
                    )
                )
                set_saved_data(line_id, LINECommunicationStateSchema(
                    state=STATUS.INPUT_IMPRESSION.name,
                    data={
                        "report_id": report.id
                    }
                ))


@router.on_event("startup")
async def startup():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mentoring_start_messages, 'interval', minutes=1)
    scheduler.start()
