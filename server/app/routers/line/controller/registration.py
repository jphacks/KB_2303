from datetime import timedelta, datetime

from linebot.v3.messaging import (
    TextMessage,
    TemplateMessage, ButtonsTemplate, MessageAction, ConfirmTemplate, CarouselTemplate, CarouselColumn, Sender
)

from crud.schemas import LINECommunicationStateSchema
from db import schemas
from db.crud import user as user_crud, group as group_crud
from db.crud.group import get_by_user_invite_token
from routers.line.model.state import STATUS
from routers.line.util.session import (
    set_saved_data,
    delete_saved_data
)
from ..data import MENTORS
from ..data.base import MentorBase


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


def registration_controller(
        saved_data: LINECommunicationStateSchema | None,
        line_id: str,
        input_text: str,
        mentor: MentorBase,
        db: any):
    reply_message_list = []

    # 初期状態である場合
    if saved_data is None:
        # はじめると送られているか
        if input_text == "はじめる":
            # GroupID入力へ移行
            reply_message_list.append(TextMessage(
                text=mentor.RESPONSE_ASK_GROUP_ID)
            )
            # 状態を更新
            set_saved_data(line_id, LINECommunicationStateSchema(
                state=STATUS.INPUT_GROUP_ID.name,
                data={}
            ))

        else:
            reply_message_list.append(TextMessage(
                text=mentor.RESPONSE_REQUEST_START_REGISTRATION)
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
                    text=mentor.RESPONSE_WRONG_GROUP_ID
                ))

            # グループが存在した場合、グループに参加するか確認する
            else:
                message = mentor.build(
                    mentor.RESPONSE_CONFIRM_GROUP_JOIN,
                    {"GROUP_NAME": group.name}
                )
                reply_message_list.append(TextMessage(
                    text=message
                ))
                reply_message_list.append(TemplateMessage(
                    alt_text=message,
                    template=ConfirmTemplate(
                        text="選択してください",
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
                # メンターを聞く
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_ASK_MENTOR)
                )
                reply_message_list.append(TemplateMessage(
                    alt_text="選択してください",
                    template=CarouselTemplate(
                        image_size="cover",
                        columns=[
                            CarouselColumn(
                                thumbnail_image_url=f"{mentor.IMG_DOMAIN}{mentor.ICON_PATH}",
                                title=f"{mentor.NAME}メンター",
                                text=mentor.DESCRIPTION,
                                actions=[
                                    MessageAction(
                                        label="選択",
                                        text=str(mentor_id)
                                    )
                                ]
                            ) for mentor_id, mentor in MENTORS.items() if mentor_id > 0]
                    )
                ))
                # 状態を更新
                saved_data.state = STATUS.SELECT_MENTOR.name
                set_saved_data(line_id, saved_data)

            # 参加しない場合
            elif input_text == "いいえ":
                # 再入力を求める
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_CANCEL_GROUP_JOIN)
                )
                # 状態を更新
                saved_data.state = STATUS.INPUT_GROUP_ID.name
                del saved_data.data["group_id"]
                set_saved_data(line_id, saved_data)

            # どちらでもない場合
            else:
                # グループに参加するか確認する
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_REQUEST_BOOLEAN)
                )
        # キャラクターを選択していた場合
        elif saved_status == STATUS.SELECT_MENTOR:
            if input_text == "":
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_REQUEST_SELECT
                ))
            else:
                mentor = MENTORS[int(input_text)]

                sender = Sender(
                    name=mentor.NAME
                )

                if mentor.ICON_PATH is not None:
                    sender.icon_url = f"{mentor.IMG_DOMAIN}{mentor.ICON_PATH}"

                # 挨拶
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_GREETING,
                    sender=sender
                ))
                # 氏名を聞く
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_ASK_NAME,
                    sender=sender
                ))
                # 状態を更新
                saved_data.state = STATUS.INPUT_NAME.name
                saved_data.data["mentor_id"] = int(input_text)
                set_saved_data(line_id, saved_data)

        # 氏名を聞いていた場合
        elif saved_status == STATUS.INPUT_NAME:
            if input_text == "":
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_REQUEST_TEXT)
                )
            else:
                # 目標を聞く
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_ASK_GOAL)
                )
                # 状態を更新
                saved_data.state = STATUS.INPUT_GOAL.name
                saved_data.data["name"] = input_text
                set_saved_data(line_id, saved_data)

        # 目標を聞いていた場合
        elif saved_status == STATUS.INPUT_GOAL:
            if input_text == "":
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_REQUEST_TEXT)
                )
            else:
                # メンタリングの頻度を聞く
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_ASK_INTERVAL
                ))

                reply_message_list.append(TemplateMessage(
                    alt_text="頻度を選択",
                    template=ButtonsTemplate(
                        text="選択してください",
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
                    text=mentor.RESPONSE_REQUEST_SELECT)
                )
            else:
                # 短期目標を聞く
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_ASK_TARGET)
                )
                # 状態を更新
                saved_data.state = STATUS.INPUT_TARGET.name
                saved_data.data["interval_days"] = int(input_text)
                set_saved_data(line_id, saved_data)

        # 短期目標を聞いていた場合
        elif saved_status == STATUS.INPUT_TARGET:
            if input_text == "":
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_REQUEST_TEXT)
                )
            else:
                # 状態を代入
                saved_data.state = STATUS.CONFIRM_REGISTRATION.name
                saved_data.data["target"] = input_text

                # 登録内容を確認

                reply_text_build = mentor.build(
                    mentor.RESPONSE_CONFIRM_REGISTRATION,
                    {"DATA": confirm_data(saved_data)}
                )
                reply_message_list.append(TextMessage(
                    text=reply_text_build
                ))
                reply_message_list.append(TemplateMessage(
                    alt_text="確定確認",
                    template=ConfirmTemplate(
                        text="選択してください",
                        actions=[
                            MessageAction(
                                label="確定",
                                text="確定する"
                            ),
                            MessageAction(
                                label="修正",
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
                        mentor_id=saved_data.data["mentor_id"]
                    )
                )

                # グループに登録
                group_crud.join_user(
                    db,
                    group_crud.get(db, saved_data.data["group_id"]),
                    user
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
                    text=mentor.RESPONSE_COMPLETE_REGISTRATION)
                )
            elif input_text == "修正する":
                # 氏名の入力に戻るか確認
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_CONFIRM_RETURN_TO_INPUT_NAME
                ))

                reply_message_list.append(TemplateMessage(
                    alt_text=mentor.RESPONSE_CONFIRM_RETURN_TO_INPUT_NAME,
                    template=ConfirmTemplate(
                        text="選択してください",
                        actions=[
                            MessageAction(
                                label="やり直す",
                                text="やり直す"
                            ),
                            MessageAction(
                                label="やめる",
                                text="やめる"
                            )
                        ]
                    )
                ))
                # 状態を更新
                saved_data.state = STATUS.CONFIRM_RETURN_TO_INPUT_NAME.name
                set_saved_data(line_id, saved_data)
            else:
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_REQUEST_SELECT)
                )

        # 氏名の入力に戻るか確認をしていた場合
        elif saved_status == STATUS.CONFIRM_RETURN_TO_INPUT_NAME:
            if input_text == "やり直す":
                # 氏名を聞く
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_ASK_NAME
                ))
                # 状態を更新
                saved_data.state = STATUS.INPUT_NAME.name
                set_saved_data(line_id, saved_data)

            elif input_text == "やめる":
                # 状態を代入
                saved_data.state = STATUS.CONFIRM_REGISTRATION.name

                # 登録内容を確認
                reply_text_build = mentor.build(
                    mentor.RESPONSE_CONFIRM_REGISTRATION,
                    {"DATA": confirm_data(saved_data)}
                )
                reply_message_list.append(TextMessage(
                    text=reply_text_build
                ))
                reply_message_list.append(TemplateMessage(
                    alt_text="確定確認",
                    template=ConfirmTemplate(
                        text="選択してください",
                        actions=[
                            MessageAction(
                                label="確定",
                                text="確定する"
                            ),
                            MessageAction(
                                label="修正",
                                text="修正する"
                            )
                        ]
                    )
                ))
                # 状態を更新
                set_saved_data(line_id, saved_data)
            else:
                reply_message_list.append(TextMessage(
                    text=mentor.RESPONSE_REQUEST_SELECT)
                )

    return reply_message_list
