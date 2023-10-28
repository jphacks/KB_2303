class MentorBase:
    ID = None
    NAME = "てるみー"

    PROMPT = None

    FULL_IMG_PATH = None
    ICON_PATH = None

    # ------
    # 登録処理
    # ------

    # 登録開始時(グループID聴取)のメッセージ
    RESPONSE_REQUEST_START_REGISTRATION = "「はじめる」と入力してください！"
    RESPONSE_ASK_GROUP_ID = "管理者から発行されたグループIDを入力してください！"
    RESPONSE_WRONG_GROUP_ID = "グループIDが間違っているようです....\nもう一度入力してください！"

    # グループ参加確認時のメッセージ
    RESPONSE_CONFIRM_GROUP_JOIN = "<<GROUP_NAME>>に参加しますか？"
    RESPONSE_CANCEL_GROUP_JOIN = "参加をキャンセルしました！再度グループIDを入力してください！"

    # メンター選択時のメッセージ
    RESPONSE_ASK_MENTOR = "あなたを担当させていただくメンターを選択してください！"

    # 選択された後のあいさつ
    RESPONSE_GREETING = f"はじめまして、{NAME}です！これから一緒に頑張りましょう！"

    # 氏名入力
    RESPONSE_ASK_NAME = "あなたのお名前を教えてください！"

    # 目標入力
    RESPONSE_ASK_GOAL = "あなたがこれから達成したい目標を教えてください！"

    # メンタリング頻度入力
    RESPONSE_ASK_INTERVAL = "私は何日ごとにあなたにお声がけすれば良いでしょうか？"

    # 短期目標入力
    RESPONSE_ASK_TARGET = "では、次にお声がけするまでに達成したいことを具体的に教えてください！"

    # 登録内容確認
    RESPONSE_CONFIRM_REGISTRATION = "以下の内容で登録させていただきますが、よろしいですか？\n<<DATA>>"

    # 登録完了
    RESPONSE_COMPLETE_REGISTRATION = "登録が完了しました！それでは、これからよろしくお願いします！"

    RESPONSE_CONFIRM_RETURN_TO_INPUT_NAME = "お名前からもう一度お伺いしますが、よろしいですか？"

    # ------
    # メンタリング
    # ------
    # プッシュ時
    RESPONSE_PUSH_START = "こんにちは！本日のメンタリングを行わせていただきます！"
    RESPONSE_PUSH_HEARING = "最近の様子を教えてください！（例: 調子が良かった、悪かった、など）"

    # -----
    # 共通
    # -----
    RESPONSE_REQUEST_BOOLEAN = "お手数ですが、「はい」か「いいえ」でお答えいただけますと幸いです!"
    RESPONSE_REQUEST_SELECT = "お手数ですが、上のボタンからの選択をお願いします！"
    RESPONSE_REQUEST_TEXT = "お手数ですが、テキストでの入力をお願いします！"

    @staticmethod
    def build(template_string: str, data: dict[str, str]) -> str:
        for key, value in data.items():
            template_string = template_string.replace(f"<<{key}>>", value)
        return template_string
