from datetime import datetime, timedelta

from linebot.v3.messaging import (
    TextMessage
)

from crud.schemas import LINECommunicationStateSchema
from db import models
from db.crud import report as report_crud, user as user_crud
from db.schemas import ScheduledReport
from routers.line.model.state import STATUS
from routers.line.util.session import (
    set_saved_data
)
from util import gptclient
from ..data.base import MentorBase


def confirm_data(saved_data: LINECommunicationStateSchema):
    return "\n".join(list(map(str, [
        f'次回までの目標:',
        saved_data.data["next_target"]
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
        saved_data.state = STATUS.INPUT_ACHIEVED_SCORE.name
        set_saved_data(line_id, saved_data)

        # 所感に対する返答を作成
        chatgpt_response = gptclient.gptchat(
            text="\n".join([
                "あなたは、以下の特徴を持つ上司として一人の部下の学習進捗を確認してください。",
                f"特徴: {mentor.PROMPT}",
                "",
                "学習者の定期報告の中で、最近の様子について尋ねたところ、以下の返答が得られました。",
                f"「{input_text}」",
                "",
                "この学習者の返答に対して、学習者を褒め、問題点を指摘して、改善のためのアイデアを提供できるよう、適切な返答を行ってください。",
                "",
                f"なお、この学習者は「{user.config.goal}」を目標としており、この定期報告までに「{report.target}」を達成することを目標としています。",
                "",
                "文字数は150文字以内で、学習者に伝えるメッセージだけを、鉤括弧等を含めずに出力してください。なお、新たな問いかけを行うことは禁じます。"
            ])
        )

        # 返答を保存
        saved_data.data["impression_feedback"] = chatgpt_response

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

        # 状態更新
        saved_data.state = STATUS.INPUT_REASON.name
        set_saved_data(line_id, saved_data)

    # 理由を聞いていた場合
    elif saved_status == STATUS.INPUT_REASON:
        # 理由を保存
        saved_data.data["reason"] = input_text
        saved_data.state = STATUS.INPUT_PROBLEM.name
        set_saved_data(line_id, saved_data)

        # 理由に対する返答を作成
        chatgpt_response = gptclient.gptchat(
            text="\n".join([
                "あなたは、以下の特徴を持つ上司として一人の部下の学習進捗を確認してください。",
                f"特徴: {mentor.PROMPT}",
                "",
                f"学習者の定期報告の中で、この定期報告までに達成すべき目標であった「{report.target}」をどの程度達成したかについて尋ねたところ、{saved_data.data['achieved_score']}%程度であると答えました。",
                "次に、この達成度を答えた理由について尋ねたところ、以下の返答が得られました。",
                f"「{input_text}」",
                "",
                "この学習者の返答に対して、学習者を褒め、問題点を指摘して、改善のためのアイデアを提供できるよう、適切な返答を行ってください。",
                "",
                f"なお、この学習者は「{user.config.goal}」を最終的な目標としています。",
                ""
                f"また、この学習者は直近の数日間を振り返って{saved_data.data['impression']}と答え、"
                f"あなたはそれに{saved_data.data['impression_feedback']}と答えました。"
                "",
                "文字数は150文字以内で、学習者に伝えるメッセージだけを、鉤括弧等を含めずに出力してください。なお、新たな問いかけを行うことは禁じます。"
            ])
        )

        # 返答を保存
        saved_data.data["reason_feedback"] = chatgpt_response

        reply_message_list.append(TextMessage(
            text=chatgpt_response
        ))

        # 困りごとを聞く
        reply_message_list.append(TextMessage(
            text=mentor.RESPONSE_ASK_PROBLEM
        ))

    # 困りごとを聞いていた場合
    elif saved_status == STATUS.INPUT_PROBLEM:
        # 困りごとを保存
        saved_data.data["problem"] = input_text
        saved_data.state = STATUS.INPUT_HELP_REQUIRED.name
        set_saved_data(line_id, saved_data)

        # 困りごとに対する返答を作成
        chatgpt_response = gptclient.gptchat(
            text="\n".join([
                "あなたは、以下の特徴を持つ上司として一人の部下の学習進捗を確認してください。",
                f"特徴: {mentor.PROMPT}",
                "",
                "学習者の定期報告の中で、困っていることについて尋ねたところ、以下の返答が得られました。",
                f"「{input_text}」",
                "",
                "この学習者の返答に対して、学習者を褒め、問題点を指摘して、改善のためのアイデアを提供できるよう、適切な返答を行ってください。",
                "",
                f"なお、この学習者は「{user.config.goal}」を最終的な目標としています。",
                ""
                f"また、この学習者は直近の数日間を振り返って{saved_data.data['impression']}と答え、"
                f"あなたはそれに{saved_data.data['impression_feedback']}と答えました。",
                ""
                f"更に、この学習者はこの定期報告までに達成すべき目標であった「{report.target}」をどの程度達成したかについて尋ねたところ、{saved_data.data['achieved_score']}%程度であると答えました。",
                "次に、この達成度を答えた理由について尋ねたところ、以下の返答が得られています。",
                f"「{saved_data.data['reason']}」",
                "",
                "文字数は150文字以内で、学習者に伝えるメッセージだけを、鉤括弧等を含めずに出力してください。なお、新たな問いかけを行うことは禁じます。"
            ])
        )

        # 返答を保存
        saved_data.data["problem_feedback"] = chatgpt_response

        reply_message_list.append(TextMessage(
            text=chatgpt_response
        ))

        # 管理者への助けを求めるかを聞く
        reply_message_list.append(TextMessage(
            text=mentor.RESPONSE_ASK_HELP_REQUIRED
        ))

    # 管理者への助けを求めるかを聞いていた場合
    elif saved_status == STATUS.INPUT_HELP_REQUIRED:
        # 管理者への助けを求めるかを保存
        if input_text == "はい":
            saved_data.data["help_required"] = True
            response_text = mentor.RESPONSE_HELP_NEEDED
        else:
            saved_data.data["help_required"] = False
            response_text = mentor.RESPONSE_HELP_NOT_NEEDED

        # 管理者への助けを求めるかに対する返答を作成
        reply_message_list.append(TextMessage(
            text=response_text
        ))

        # 次回の目標をヒアリング
        reply_message_list.append(TextMessage(
            text=mentor.RESPONSE_ASK_NEXT_TARGET
        ))

        # 次回の目標を聞く状態に遷移
        saved_data.state = STATUS.INPUT_NEXT_TARGET.name
        set_saved_data(line_id, saved_data)

    # 次回の目標を聞いていた場合
    elif saved_status == STATUS.INPUT_NEXT_TARGET:
        # 空文字の場合は聞き直し
        if input_text == "":
            reply_message_list.append(TextMessage(
                text=mentor.RESPONSE_REQUEST_TEXT
            ))
            return reply_message_list
        else:
            # 状態更新
            saved_data.data["target"] = input_text
            saved_data.state = STATUS.CONFIRM_NEXT_TARGET.name
            set_saved_data(line_id, saved_data)

            # 確認メッセージを作成
            confirm_message = mentor.RESPONSE_CONFIRM_NEXT_TARGET.replace(
                "<<DATA>>",
                confirm_data(saved_data)
            )

            # 確認メッセージを送信
            reply_message_list.append(TextMessage(
                text=confirm_message
            ))

    # 次回の目標を確認していた場合
    elif saved_status == STATUS.CONFIRM_NEXT_TARGET:
        # 確認メッセージを送信
        if input_text == "はい":

            # メンタリング完了
            report.hearing_date = datetime.now()
            report.impression = saved_data.data["impression"]
            report.impression_feedback = saved_data.data["impression_feedback"]
            report.achieved_score = saved_data.data["achieved_score"]
            report.reason = saved_data.data["reason"]
            report.reason_feedback = saved_data.data["reason_feedback"]
            report.problem = saved_data.data["problem"]
            report.problem_feedback = saved_data.data["problem_feedback"]
            report.help_required = saved_data.data["help_required"]

            report_crud.update(db, report)

            user_crud.create_report(db, user, ScheduledReport(
                target=saved_data.data["target"],
                scheduled_hearing_date=datetime.now() + timedelta(days=user.config.interval_days)
            ))

            # メッセージ送信
            reply_message_list.append(TextMessage(
                text=mentor.RESPONSE_COMPLETE_REGISTRATION
            ))

            # 状態更新
            saved_data.state = STATUS.INPUT_IMPRESSION.name
            set_saved_data(line_id, saved_data)

        else:
            # 状態更新
            saved_data.state = STATUS.INPUT_NEXT_TARGET.name
            set_saved_data(line_id, saved_data)

            # 確認メッセージを作成
            reply_message_list.append(TextMessage(
                text=mentor.RESPONSE_CONFIRM_NEXT_TARGET.replace(
                    "<<DATA>>",
                    confirm_data(saved_data)
                )
            ))

    return reply_message_list
