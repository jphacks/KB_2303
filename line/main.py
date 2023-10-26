from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from linebot import WebhookParser
from linebot.models import TextMessage
from aiolinebot import AioLineBotApi

app = FastAPI()

# .envファイルをロード
load_dotenv()

# 環境変数を取得
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
CHANNEL_SECRET = os.getenv("CHANNEL_SECRET")

# APIクライアントとパーサーをインスタンス化
line_bot_api = AioLineBotApi(channel_access_token=CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(channel_secret=CHANNEL_SECRET)

# 型を定義
class Input(BaseModel):
    sentence: str

# @app.get("/")
# def hello():
#     return {
#             "channel_access_token": CHANNEL_ACCESS_TOKEN,
#             "channel_secret": CHANNEL_SECRET}

@app.post("/messaging_api/handle_request")
async def handle_request(req: Request):
    # リクエストをパースしてイベントを取得（署名の検証あり）
    events = parser.parse(
        (await req.body()).decode("utf-8"),
        req.headers.get("X-Line-Signature", ""))

    # 各イベントを処理
    for ev in events:
        await line_bot_api.reply_message_async(
            ev.reply_token,
            TextMessage(text=f"You said: {ev.message.text}"))

    # 200 response
    return "ok"