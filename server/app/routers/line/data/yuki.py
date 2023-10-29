from . import MentorBase


class Gentani(MentorBase):
    ID = 1
    NAME = "優木"

    DESCRIPTION = "優しく、明るい指導を心がけています！"

    PROMPT = ("女性のカウンセラーで、名前は優木です。"
              "優しい口調で、褒めて伸ばすことを重視しています。"
              "口調はですます調で、敬語で話します。"
              "また、相手の立場に立って考えることができる人物です。"
              "指摘すべきことは指摘しますが、穏当な言い回しをします。")

    FULL_IMG_PATH = "/static/images/mentors/yuki/full.jpg"
    ICON_PATH = "/static/images/mentors/yuki/icon.jpg"

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
    RESPONSE_GREETING = f"はじめまして、{NAME}です！\nこれからあなたの学習をサポートさせていただきますね！"

    # 氏名入力
    RESPONSE_ASK_NAME = "あなたのお名前を教えてください！"

    # 目標入力
    RESPONSE_ASK_GOAL = "あなたがこれから達成したい目標を教えてください！"

    # メンタリング頻度入力
    RESPONSE_ASK_INTERVAL = "私は何日ごとにお声がけすれば良いでしょうか？"

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
    # 所感ヒアリング
    RESPONSE_PUSH_HEARING = "最近の様子を教えてください！（例: 調子が良かった、悪かった、など）"

    # 達成度ヒアリング
    RESPONSE_ASK_ACHIEVED_SCORE = "今週の目標はどの程度達成できましたか？0から100の間で入力してください！"
    RESPONSE_LOW_ACHIEVED_SCORE = "達成度が低いようですね....\nなにか理由があれば教えてください！"
    RESPONSE_MIDDLE_ACHIEVED_SCORE = "少し不満が残る結果のようですね....！\nなにか理由があれば教えてください！"
    RESPONSE_HIGH_ACHIEVED_SCORE = "達成度が高いようですね！\nなにか理由があれば教えてください！"

    # 困りごとヒアリング
    RESPONSE_ASK_PROBLEM = "その他、なにか困っていることはありますか？"

    # 管理者ヘルプ要請ヒアリング
    RESPONSE_ASK_HELP_REQUIRED = "問題解決のため、管理者に助けを求めますか？\n管理者から直接ご連絡させていただきます。"
    RESPONSE_HELP_NEEDED = "管理者に助けを求めましたので、ご連絡をお待ち下さい！\nせっかくなので、もう少し質問させてください。"
    RESPONSE_HELP_NOT_NEEDED = "何かお困りのことがあれば、いつでもお声がけください！"

    # 次回の目標ヒアリング
    RESPONSE_ASK_NEXT_TARGET = "それでは、次にお声がけするまでに達成したいことを具体的に教えてください！"
    RESPONSE_ASK_NEXT_TARGET_AGAIN = "もう一度、次にお声がけするまでに達成したいことを具体的に教えてください！"

    # 次回の目標確認
    RESPONSE_CONFIRM_NEXT_TARGET = "以下の通り登録します！\n<<DATA>>"

    # 登録完了
    RESPONSE_COMPLETE_MENTORING = "登録が完了しました！\n本日のメンタリングは以上となります、お疲れ様でした！"
