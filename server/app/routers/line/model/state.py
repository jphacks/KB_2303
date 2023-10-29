from enum import Enum


# "10101" 上1桁：1-ユーザの登録,2-定期メンタリング 上23桁：処理順 上45桁：同処理で分岐する場合1ずつ加算する
class STATUS(Enum):
    # 1xxxx: ユーザの登録
    INPUT_GROUP_ID = 10101  # グループIDを聞く
    CONFIRM_GROUP_JOIN = 10102  # グループに参加するか確認
    SELECT_MENTOR = 10201
    INPUT_NAME = 10301  # 氏名を聞く
    INPUT_GOAL = 10401  # 目標を聞く
    INPUT_INTERVAL = 10501  # メンタリングの頻度を聞く
    INPUT_TARGET = 10601  # 短期目標を聞く
    CONFIRM_REGISTRATION = 10701  # 登録内容を確認
    CONFIRM_RETURN_TO_INPUT_NAME = 10702  # 氏名の入力に戻るか確認

    # 2xxxx: 定期メンタリング
    INPUT_IMPRESSION = 20101  # メンタリング開始・所感ヒアリング
    INPUT_ACHIEVED_SCORE = 20201  # 達成度を聞く
    INPUT_REASON = 20301  # 達成度の理由を聞く
    INPUT_PROBLEM = 20401  # 困りごとを聞く
    INPUT_HELP_REQUIRED = 20501  # ヘルプ要請を聞く
    INPUT_NEXT_TARGET = 20601  # 次回の目標を聞く
    CONFIRM_NEXT_TARGET = 20701  # 次回の目標を確認
