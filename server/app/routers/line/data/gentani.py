from . import MentorBase


class Gentani(MentorBase):
    ID = 1
    NAME = "厳谷"

    DESCRIPTION = "厳しく指導します。"

    PROMPT = ("男性のカウンセラーで、名前は厳谷です。"
              "厳しい指導を行いますが、評価すべき箇所についてはしっかりと褒める人物です。"
              "口調はですます調で、敬語を使うことが多いです。"
              "また、相手の立場に立って考えることができる人物です。"
              "口調の厳しさについては、目標達成のためには場合によっては厳しく指導する必要があると考えているためです。")

    FULL_IMG_PATH = "/static/images/mentors/gentani/full.jpg"
    ICON_PATH = "/static/images/mentors/gentani/icon.jpg"

    # ------
    # 登録処理
    # ------

    # 登録開始時(グループID聴取)のメッセージ
    RESPONSE_REQUEST_START_REGISTRATION = "登録を行う場合は「はじめる」と入力してください。"
    RESPONSE_ASK_GROUP_ID = "管理者から発行されたグループIDを入力してください。"
    RESPONSE_WRONG_GROUP_ID = "グループIDが間違っているようです。\nもう一度入力してください"

    # グループ参加確認時のメッセージ
    RESPONSE_CONFIRM_GROUP_JOIN = "<<GROUP_NAME>>に参加しますか？"
    RESPONSE_CANCEL_GROUP_JOIN = "参加をキャンセルしましたので、再度グループIDを入力してください。"

    # メンター選択時のメッセージ
    RESPONSE_ASK_MENTOR = "あなたを担当させていただくメンターを選択してください。"

    # 選択された後のあいさつ
    RESPONSE_GREETING = f"はじめまして、{NAME}です。これから一緒に頑張りましょう。"

    # 氏名入力
    RESPONSE_ASK_NAME = "あなたのお名前を教えてください。"

    # 目標入力
    RESPONSE_ASK_GOAL = "あなたがこれから達成したい目標を教えてください。"

    # メンタリング頻度入力
    RESPONSE_ASK_INTERVAL = "私は何日ごとにあなたにお声がけすれば良いでしょうか？"

    # 短期目標入力
    RESPONSE_ASK_TARGET = "では、次にお声がけするまでに達成したいことを具体的に教えてください。"

    # 登録内容確認
    RESPONSE_CONFIRM_REGISTRATION = "以下の内容で登録させていただきますが、よろしいですか？\n<<DATA>>"

    # 登録完了
    RESPONSE_COMPLETE_REGISTRATION = "登録が完了しました。それでは、これからよろしくお願いします。"

    RESPONSE_CONFIRM_RETURN_TO_INPUT_NAME = "お名前からもう一度お伺いしますが、よろしいですか？"

    # ------
    # メンタリング
    # ------
    # プッシュ時
    RESPONSE_PUSH_START = "こんにちは。本日のメンタリングを行わせていただきます。"
    # 所感ヒアリング
    RESPONSE_PUSH_HEARING = "まずは、最近の様子を教えてください。（例: 調子が良かった、悪かった、など）"

    # 達成度ヒアリング
    RESPONSE_ASK_ACHIEVED_SCORE = "今週の目標はどの程度達成できましたか？0から100の間で入力してください。"
    RESPONSE_LOW_ACHIEVED_SCORE = "達成度が低いようですね。\nなにか理由があれば教えてください。"
    RESPONSE_MIDDLE_ACHIEVED_SCORE = "少し不満が残る結果のようですね。\nなにか理由があれば教えてください。"
    RESPONSE_HIGH_ACHIEVED_SCORE = "達成度が高いようですね。\nなにか理由があれば教えてください。"

    # 困りごとヒアリング
    RESPONSE_ASK_PROBLEM = "その他、なにか困っていることはありますか？"

    # 管理者ヘルプ要請ヒアリング
    RESPONSE_ASK_HELP_REQUIRED = "問題解決のため、こちらから管理者にお声がけしたほうがよろしいでしょうか？\nご希望の場合は、管理者より直接ご連絡させていただきます。"
    RESPONSE_HELP_NEEDED = "それでは、後ほど管理者に伝えておきます！\n折角の機会ですから、次の目標も設定しましょう。"
    RESPONSE_HELP_NOT_NEEDED = "何かお困りのことがあれば、いつでもお声がけください。"

    # 次回の目標ヒアリング
    RESPONSE_ASK_NEXT_TARGET = "最後に、次にお声がけするまでに達成したいことを具体的に教えてください。"
    RESPONSE_ASK_NEXT_TARGET_AGAIN = "もう一度、次にお声がけするまでに達成したいことを具体的に教えてください。"

    # 次回の目標確認
    RESPONSE_CONFIRM_NEXT_TARGET = "以下の通り登録します。\n<<DATA>>"

    # 登録完了
    RESPONSE_COMPLETE_MENTORING = "登録が完了しました。\n本日のメンタリングは以上となります、お疲れ様でした！引き続き頑張っていきましょう！"

    # -----
    # 共通
    # -----
    RESPONSE_REQUEST_BOOLEAN = "お手数ですが、「はい」か「いいえ」でお答えいただけますと幸いです！"
    RESPONSE_REQUEST_SELECT = "お手数ですが、上のボタンからの選択をお願いします！"
    RESPONSE_REQUEST_TEXT = "お手数ですが、テキストでの入力をお願いします！"

    RESPONSE_INACTIVE = "次回のご連絡をお待ち下さい！"


class Teru(MentorBase):
    ID = 2
    NAME = "テル"

    DESCRIPTION = "優しく指導します。"

    PROMPT = ("男性のカウンセラーで、名前はテルです。"
              "いつも楽しそうに話しますが評価すべき箇所についてはしっかりと褒める人物です。"
              "高校までアメリカに住んでいたため口調は翻訳調でダヨなどカタカナを語尾につけることが多いです。"
              "また、相手の立場に立って考えることができる人物です。"
              "口調の厳しさについては、目標達成のためには場合によっては厳しく指導する必要があると考えているためです。")

    FULL_IMG_PATH = "/static/images/mentors/gentani/full.jpg"
    ICON_PATH = "/static/images/mentors/gentani/icon.jpg"

    # ------
    # 登録処理
    # ------

    # 登録開始時(グループID聴取)のメッセージ
    RESPONSE_REQUEST_START_REGISTRATION = "登録を行う場合は「はじめる」と入力してください。"
    RESPONSE_ASK_GROUP_ID = "管理者から発行されたグループIDを入力してください。"
    RESPONSE_WRONG_GROUP_ID = "グループIDが間違っているようです。\nもう一度入力してください"

    # グループ参加確認時のメッセージ
    RESPONSE_CONFIRM_GROUP_JOIN = "<<GROUP_NAME>>に参加しますか？"
    RESPONSE_CANCEL_GROUP_JOIN = "参加をキャンセルしましたので、再度グループIDを入力してください。"

    # メンター選択時のメッセージ
    RESPONSE_ASK_MENTOR = "あなたを担当させていただくメンターを選択してください。"

    # 選択された後のあいさつ
    RESPONSE_GREETING = f"はじめまして、{NAME}です。これから一緒によろしくお願いしますね！"

    # 氏名入力
    RESPONSE_ASK_NAME = "あなたのお名前を教えてほしいナ。"

    # 目標入力
    RESPONSE_ASK_GOAL = "あなたがこれからできるようになりたい目標を教えてヨ。"

    # メンタリング頻度入力
    RESPONSE_ASK_INTERVAL = "スケジュールを決めたいと思います。何日ごとにあなたに連絡すればいいカナ？"

    # 短期目標入力
    RESPONSE_ASK_TARGET = "じゃあ次に連絡するまでにやりたいことを具体的に教えてヨ。"

    # 登録内容確認
    RESPONSE_CONFIRM_REGISTRATION = "以下の内容で登録しちゃうけど、いい？\n<<DATA>>"

    # 登録完了
    RESPONSE_COMPLETE_REGISTRATION = "登録したヨ！これからよろしくネ！"

    RESPONSE_CONFIRM_RETURN_TO_INPUT_NAME = "情報がうまく取れなかったからもう一回名前を聞きたいけどイイかな？"

    # ------
    # メンタリング
    # ------
    # プッシュ時
    RESPONSE_PUSH_START = "コンニチハ！。本日のメンタリングをやるヨ！"
    # 所感ヒアリング
    RESPONSE_PUSH_HEARING = "まずは、ユーの最近の様子を教えてほしいナ。（たとえば: 調子が良かった、悪かった、とか、）"

    # 達成度ヒアリング
    RESPONSE_ASK_ACHIEVED_SCORE = "今週の目標はどの程度達成できましたかナ？0から100の間で入力してほしいヨ。"
    RESPONSE_LOW_ACHIEVED_SCORE = "達成度が低いようだね。\nなにか理由があったら聞きたいナ。"
    RESPONSE_MIDDLE_ACHIEVED_SCORE = "少し不満が残る結果のようですね。\nなにか理由があるのかい？"
    RESPONSE_HIGH_ACHIEVED_SCORE = "すごいじゃないか！\nうまくいったのになにかワケがあれば教えてヨ。"

    # 困りごとヒアリング
    RESPONSE_ASK_PROBLEM = "その他に、なにか困っていることはある？"

    # 管理者ヘルプ要請ヒアリング
    RESPONSE_ASK_HELP_REQUIRED = "問題解決のため、管理者にも助けを求めますか？\nご希望の場合は、直接ご連絡させていただきます。"
    RESPONSE_HELP_NEEDED = "管理者に通知しましたので、ご連絡をお待ち下さい。\n折角の機会ですから、次の目標も設定しましょう。"
    RESPONSE_HELP_NOT_NEEDED = "何かお困りのことがあれば、いつでもお声がけください。"

    # 次回の目標ヒアリング
    RESPONSE_ASK_NEXT_TARGET = "最後に、次にお声がけするまでに達成したいことを具体的に教えてください。"
    RESPONSE_ASK_NEXT_TARGET_AGAIN = "もう一度、次にお声がけするまでに達成したいことを具体的に教えてください。"

    # 次回の目標確認
    RESPONSE_CONFIRM_NEXT_TARGET = "以下の通り登録します。\n<<DATA>>"

    # 登録完了
    RESPONSE_COMPLETE_MENTORING = "登録が完了しました。\n本日のメンタリングは以上となります、お疲れ様でした。引き続き頑張ってください。"

    # -----
    # 共通
    # -----
    RESPONSE_REQUEST_BOOLEAN = "お手数ですが、「はい」か「いいえ」でお答えいただけますと幸いです。"
    RESPONSE_REQUEST_SELECT = "お手数ですが、上のボタンからの選択をお願いします。"
    RESPONSE_REQUEST_TEXT = "お手数ですが、テキストでの入力をお願いします。"

    RESPONSE_INACTIVE = "次回のご連絡をお待ち下さい。"
