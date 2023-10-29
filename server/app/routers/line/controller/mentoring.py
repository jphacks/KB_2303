from linebot.v3.messaging import (
    TextMessage
)

from crud.schemas import LINECommunicationStateSchema
from db.crud import report as report_crud
from routers.line.model.state import STATUS
from routers.line.util.session import (
    set_saved_data
)
from util import gptclient
from ..data.base import MentorBase
from db import models


def confirm_data(saved_data: LINECommunicationStateSchema):
    return "\n".join(list(map(str, [
        f'氏名:',
        saved_data.data["name"],
        "",
        f'目標:',
        saved_data.data["goal"],
        "",
        f'メンタリングの頻度:',
        f'{saved_data.data["interval_days"]}日に1回',
        "",
        f'{saved_data.data["interval_days"]}日後までの目標:',
        saved_data.data["target"]
    ])))


def mentoring_controller(
        saved_data: LINECommunicationStateSchema,
        line_id: str,
        input_text: str,
        mentor: MentorBase,
        user: models.User,
        db: any):
    reply_message_list = []

    # 状態を取得
    saved_status: STATUS = STATUS[saved_data.state]

    report = None
    if saved_data.data["report_id"] is not None:
        report = report_crud.get(db, saved_data.data["report_id"])

    # 状態に応じて処理を分岐
    # 所感を聞いていた場合
    if saved_status == STATUS.INPUT_IMPRESSION:
        # 所感を保存
        saved_data.data["impression"] = input_text
        saved_data.state = STATUS.INPUT_ACHIEVED_SCORE.value
        set_saved_data(line_id, saved_data)

        # 所感に対する返答を作成
        chatgpt_response = gptclient.gptclient(
            text="\n".join([
                "あなたは、以下の特徴を持つ上司として一人の部下の学習進捗を確認してください。",
                f"特徴: {mentor.PROMPT}",
                "",
                f"なお、この学習者は「{user.config.}」"
                "",
                "学習者の定期報告の中で、最近の様子について尋ねたところ、以下の返答が得られました。",
                f"「{input_text}」",
                "",
                "この学習者の返答に対して、学習者を褒め、問題点を指摘して、改善のためのアイデアを提供できるよう、適切な返答を行ってください。",
                "",
                "ただしあなたは教育係の代理の窓口なので、何らかの個別対応をするときは約束はせずにメッセージを担当者に取り次ぎます。",
                "文字数は150文字以内で、学習者に伝えるメッセージだけを、鉤括弧等を含めずに出力してください。なお、新たな問いかけを行うことは禁じます。"
            ])
        )
        reply_message_list.append(TextMessage(
            text=chatgpt_response
        ))

        # 達成度を聞く
        reply_message_list.append(TextMessage(
            text=mentor.RESPONSE_ASK_ACHIEVED_SCORE
        ))

    # 達成度を聞いていた場合
    elif saved_status == STATUS.INPUT_ACHIEVED_SCORE:
        # 達成度を保存
        try:
            saved_data.data["achieved_score"] = int(input_text)
        except ValueError:
            reply_message_list.append(TextMessage(
                text="達成度は0から100の間で入力してください！"
            ))
            return reply_message_list

        # 達成度に応じて返答を作成
        if saved_data.data["achieved_score"] < 50:
            reply_message_list.append(TextMessage(
                text=mentor.RESPONSE_LOW_ACHIEVED_SCORE
            ))
        elif saved_data.data["achieved_score"] < 80:
            reply_message_list.append(TextMessage(
                text=mentor.RESPONSE_MIDDLE_ACHIEVED_SCORE
            ))
        else:
            reply_message_list.append(TextMessage(
                text=mentor.RESPONSE_HIGH_ACHIEVED_SCORE
            ))

    # 理由を聞いていた場合
    elif saved_status == STATUS.INPUT_REASON:
        # 理由を保存
        saved_data.data["reason"] = input_text
        saved_data.state = STATUS.INPUT_PROBLEM.value
        set_saved_data(line_id, saved_data)

        # 理由に対する返答を作成
        chatgpt_response = gptclient.gptclient(
            text="\n".join([
                "あなたは、以下の特徴を持つ上司として一人の部下の学習進捗を確認してください。",
                f"特徴: {mentor.PROMPT}",
                "",
                "学習者の定期報告の中で、学習者は達成度の理由について尋ねたところ、以下の返答が得られました。",
                f"「{input_text}」",
                "",
                "この学習者の返答に対して、学習者を褒め、問題点を指摘して、改善のためのアイデアを提供できるよう、適切な返答を行ってください。",
                "",
                "ただしあなたは教育係の代理の窓口なので、何らかの個別対応をするときは約束はせずにメッセージを担当者に取り次ぎます。",
                "文字数は150文字以内で、学習者に伝えるメッセージだけを、鉤括弧等を含めずに出力してください。なお、新たな問いかけを行うことは禁じます。"
            ])
        )
        reply_message_list.append(TextMessage(
            text=chatgpt_response
        ))

        # 困りごとを聞く
        reply_message_list.append(TextMessage(
            text=mentor.RESPONSE_ASK_PROBLEM
        ))

    return reply_message_list
