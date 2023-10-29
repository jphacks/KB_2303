# メンタリングサポートシステム　「てるみー」

<!--[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2023/07/JPHACKS2023_ogp.png)](https://www.youtube.com/watch?v=yYRQEdfGjEg)-->
![image](https://github.com/this-code-2023/this-code/assets/37525169/c7ac1be8-e461-402f-8f6b-815ba3add747)

## 製品概要

このシステムは従来の人力のメンタリングにAIをプラスすることで、対応のきめ細やかさはそのままに人間のメンターがより多くの人を扱えるように能力を拡張するシステムである。

具体的にはメンタリングをLINEを介して定期的に、かつChatGPTを用いて自動的に行うことで、管理者の負担を大きく減らしつつ、受講生の学習管理を行うことができるシステムである。このシステムの主な機能として定期的なメッセージ送信や定期報告の自動要約、コンディションの数値化機能とそれらを閲覧する画面を備えており管理者が一度に大勢の受講生を扱えるようになっている。

また受講者はAIのメンターの人格を選ぶことで自分の性格に合ったメンターと会話できる上、簡単な質問なら人間よりレスポンスが素早く便利になる。AIが手に負えないと判断した込み入った内容は、私には対応しかねるとの返答をしつつ人間のメンターの管理画面に通知するようになっている。


### 背景(製品開発のきっかけ、課題等）

管理者が個人の学習を管理する際によく用いられる「メンタリング」は、定期的な進捗の確認やズレの原因の確認、悩みのヒアリングを行うことで、効率的な学習を促そうとするものだ。
確かにきめ細やかなメンタリングは受講者にとって有効な方法だが、同時に管理者に掛かる負担が大きく、またそれは学習者の数に比例して増していく。
メンタリング業務の中でも特に定期的に行う定期メンタリングは双方向のやり取りと入力の待ち時間が発生するため多くの時間を取られることが指摘された。
私達のチームは半数以上がメンタリングをする側に関わった経験を持っておりメンタリングの仕事量の多さを負担に感じていたためメンタリングを効率的に行うことを課題に設定した。

### 製品説明（具体的な製品の説明）



### 特長

#### 1. 特長 1

#### 2. 特長 2

#### 3. 特長 3

### 解決出来ること

### 今後の展望

### 注力したこと（こだわり等）

-
-

## 開発技術

![image](https://github.com/this-code-2023/this-code/assets/37525169/1009c52c-75e9-42fe-8221-ca2266079d06)


### 活用した技術

#### API・データ

- GPT-4  受講者との簡単なやり取りや定期報告の要約に使われる
- Natural languagge API  文章から感情分析をしてメンターの対応の優先度決定に利用する.Google製


#### フレームワーク・ライブラリ・モジュール

- Line Messaging API Python SDK
  LINEBOTのためのPythonライブラリ
- FastAPI
  APIの作成
- Nginx
  HTPS プロキシ,管理画面のファイルホスト
- PostgreSQL
  

#### デバイス

- ブラウザ
  モダンなデザインの管理画面
- LINE
  受講生のインターフェイス

### 独自技術

#### ハッカソンで開発した独自機能・技術

 スケジューリング実行機能
- AIによる柔軟な文体での報告項目
  
  プロンプトを工夫することでユーザーは人間と話しているのと同じ自由度で報告項目を報告できる。曖昧な情報をまとめて破綻なくデータベースに格納する事ができる
- メンター切り替え機能

  受講者は主に初期設定で変えられるメンターのキャラ設定によって物腰が異なるメンターと話すことができる
- アイコン変更
  
  LINEの新機能によりメンターの人格ごとにアイコンを用意して動的に切り替えられるようになった。これによって複数キャラクターが選択可能なサービスであってもキャラクターごとにアカウントを複数作る必要がなくなり、没入感がより増す。



#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）

-
-
