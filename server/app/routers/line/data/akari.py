from . import MentorBase

class Teru(MentorBase):
    ID = 3
    NAME = "あかり"

    DESCRIPTION = "優しく指導します。"

    PROMPT = ("女性のカウンセラーで、名前はテルです。"
              "基本的にクールな対応をしますが価すべき箇所についてはしっかりと褒める人物です。"
              "口調としてすこし高飛車なことが多く、わよ、頂戴など多く言います。"
              "また、相手の立場に立って考えることができる人物です。"
              "口調の厳しさについては、目標達成のためには場合によっては厳しく指導する必要があると考えているためです。")

    FULL_IMG_PATH = "/static/images/mentors/akari/full.png"
    ICON_PATH = "/static/images/mentors/akari/icon.jpg"

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
    RESPONSE_GREETING = f"はじめまして、{NAME}です。これからよろしくね"

    # 氏名入力
    RESPONSE_ASK_NAME = "お名前教えてね、フルネームで"

    # 目標入力
    RESPONSE_ASK_GOAL = "あなたがこれからできるようになりたい目標を教えてよ。"

    # メンタリング頻度入力
    RESPONSE_ASK_INTERVAL = "報告の間隔なんだけどどのくらいの頻度で連絡すればいいの"

    # 短期目標入力
    RESPONSE_ASK_TARGET = "次に連絡するまでに具体的に何をやりたいの？"

    # 登録内容確認
    RESPONSE_CONFIRM_REGISTRATION = "このの内容で登録しちゃうけど、いい？\n<<DATA>>"

    # 登録完了
    RESPONSE_COMPLETE_REGISTRATION = "登録したわよ。これからよろしく"

    RESPONSE_CONFIRM_RETURN_TO_INPUT_NAME = "ごめんなさい、もう一回名前を聞きたいけどいい？"

    # ------
    # メンタリング
    # ------
    # プッシュ時
    RESPONSE_PUSH_START = "定期メンタリング、始めるよ！"
    # 所感ヒアリング
    RESPONSE_PUSH_HEARING = "最近どう？たとえば: 調子が良かった、悪かった、とか、そういうのを言ってほしいな"

    # 達成度ヒアリング
    RESPONSE_ASK_ACHIEVED_SCORE = "今週の目標、どのくらい達成できた？パーセントで答えてね"
    RESPONSE_LOW_ACHIEVED_SCORE = "達成度が低いみたいだね。\nなにか理由があったら教えて頂戴"
    RESPONSE_MIDDLE_ACHIEVED_SCORE = "少し不満が残る結果のようね。\nなにか理由があったら教えて頂戴？"
    RESPONSE_HIGH_ACHIEVED_SCORE = "なかなかやるじゃない！\nうまくいったのになにかワケがあれば教えて頂戴。"

    # 困りごとヒアリング
    RESPONSE_ASK_PROBLEM = "困ったことある？あったら言ってね。"

    # 管理者ヘルプ要請ヒアリング
    RESPONSE_ASK_HELP_REQUIRED = "リアル管理者に助けを求める？"
    RESPONSE_HELP_NEEDED = "管理者に通知しておくわ。そのうち返信が来るでしょうね。\n折角の機会ですから、次の目標も設定しておきましょう"
    RESPONSE_HELP_NOT_NEEDED = "何か困ったことがあれば、いつでも言ってね"

    # 次回の目標ヒアリング
    RESPONSE_ASK_NEXT_TARGET = "次に連絡するまでに、具体的に何を達成したい？"
    RESPONSE_ASK_NEXT_TARGET_AGAIN = "もう一回聞くけど、次に連絡するまでに何を達成したいか言ってね頂戴"

    # 次回の目標確認
    RESPONSE_CONFIRM_NEXT_TARGET = "以下の通り登録するわよ？\n<<DATA>>"

    # 登録完了
    RESPONSE_COMPLETE_MENTORING = "登録できました！\n本日のメンタリングは終わりです。お疲れさまでした。途中で困ったことがあったら言ってくださいね"

    # -----
    # 共通
    # -----
    RESPONSE_REQUEST_BOOLEAN = "お手数ですが、「はい」か「いいえ」でお答えいただけますと幸いです。"
    RESPONSE_REQUEST_SELECT = "お手数ですが、上のボタンからの選択をお願いします。"
    RESPONSE_REQUEST_TEXT = "お手数ですが、テキストでの入力をお願いします。"

    RESPONSE_INACTIVE = "次回のご連絡をお待ち下さい。"