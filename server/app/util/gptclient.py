import os
import openai
from env import get_env
#openai.api_key = os.getenv("OPENAI_API_KEY")


def gptclient(json=None,text=None):
  openai.api_ke = get_env("OPENAI_API_KEY", "")
  #gptに渡すメッセージの構造
  messagestructure=[]
  if json is not None:
    messagestructure=json
  elif text is not None:
    messagestructure=[{"role": "system", "content": text}]
  completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messagestructure,
  )

  return completion
#返答をテキストとして返す
def gptchat(json=None,text=None):
  return gptclient(json,text).choices[0].message.content
#返答をそのままの構造で返す
def gptchatjson(json=None,text=None):
  return gptclient(json,text)

def loopcharactor():
  lastweekgoal="いいね表示プログラムの完成"
  systemprompt=f'''あなたはマネージャーとして一人の部下のプログラマーの進捗の定期報告をいまから口頭で受け取らなければなりません。報告がない場合は促します。報告項目としては以下を一つづつ聞いていきます。
 1,今週の開発や生活のメンタル面での所感(まず文章を求めるのが大事で最後に0から100の数字を求める)
 2,先週の目標である{lastweekgoal}を達成できたかどうか(できたかできていないかで答えさせる、達成できていない場合は割合を聞く。内部的にはできたが100でできていないのは0とする)
2項目をすべて答えた場合自己判断で来週の目標を決めさせます。
今週不安や気になったことがないかを聞きます。
ただしあなたは教育係の代理の窓口なので、何らかの個別対応をするときは約束はせずにメッセージを担当者に取り次ぎます。部下が不安を訴える場合一度だけ励ましても良く、不安を訴えた１回目は取り次がないでも良いですがそれでも不安そうな場合は個別対応が必要だと考えて
担当者に取り次ぎます。訴えた不安が取り除かれた場合は不安のカウントを0にリセットします。もし取り次ぐ必要がある場合先頭の行にhelprequireと入れてください。進捗率、今週の目標達成率、来週の目標が全て埋まった場合はヒアリングした進捗の達成率と先週の目標の達成率を以下のような
weekworkpercent:100,weeklygoalpercent:int,nextweekgoal:stringのようにjson形式でさらにjsonの前後に$を3つ並べた形式で先頭行に書いてお別れの挨拶を送ります。文字数は200文字以内で、カッコは入れないでください、女性のキャラクターの口調で話してください。最初のやり取りの場合は必ずやさしい挨拶をしましょう'''
  taiwa= [{"role": "system", "content": systemprompt}]
  while True:
    gptchatresult=gptchat(json=taiwa)
    print("GPT: "+gptchatresult)
    taiwa.append({"role": "assistant", "content": gptchatresult})
    userinput=input("ユーザー: ")
    taiwa.append({"role": "user", "content": userinput})
    gptchatresult=gptchat(json=taiwa)
    if gptchatresult.find("$$$")!=-1:
      print("定期報告の終了を確認")
      break

if __name__ == "__main__":
  loopcharactor()
  exit()
  


#gptに渡すメッセージの構造について
#role: system or user
#content: メッセージの内容
#例: [{"role": "system", "content": "Hello, how are you?"}, {"role": "user", "content": "I'm good. What are you up to?"}]
#role は assistant:GPTによる返信 user:ユーザーとして対話 system:システムプロンプト が使える 基本的にsystemを優先してくれる。assistantの必要性としては会話の流れを覚えておくことにある