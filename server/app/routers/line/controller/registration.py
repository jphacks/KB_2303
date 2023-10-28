from datetime import timedelta, datetime

from linebot.v3.messaging import (
    TextMessage,
    TemplateMessage, ButtonsTemplate, MessageAction
)

from crud.schemas import LINECommunicationStateSchema
from db import schemas
from db.crud import user as user_crud
from db.crud.group import get_by_user_invite_token
from routers.line.model.state import STATUS
from routers.line.util.session import (
    set_saved_data,
    delete_saved_data
)


def registration_controller(
        saved_data: LINECommunicationStateSchema | None,
        line_id: str,
        input_text: str,
        db: any):
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
                saved_data.state = STATUS.SELECT_CHARACTER.name
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
        elif saved_status == STATUS.SELECT_CHARACTER:
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
                saved_data.data["character_id"] = int(input_text)
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
                # 登録処理
                user = user_crud.create(
                    db,
                    schemas.UserCreate(
                        name=saved_data.data["name"],
                        line_id=line_id
                    )
                )
                user_crud.create_config(
                    db,
                    user,
                    schemas.UserConfigCreate(
                        interval_days=saved_data.data["interval_days"],
                        character_id=saved_data.data["character_id"]
                    )
                )

                scheduled_hearing_date = datetime.now() + timedelta(days=saved_data.data["interval_days"])
                user_crud.create_report(
                    db,
                    user,
                    schemas.ScheduledReport(
                        target=saved_data.data["target"],
                        scheduled_hearing_date=scheduled_hearing_date
                    )
                )

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

    return reply_message_list
