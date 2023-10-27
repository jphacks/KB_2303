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

if __name__ == "__main__":
  requestjson=[{"role": "system", "content": "あなたは気さくな上司として部下のプログラマーの進捗を確認してください。定期報告を提出するように求めます。文字数は150文字以内で"}]
  print(gptchat(json=requestjson))

#gptに渡すメッセージの構造について
#role: system or user
#content: メッセージの内容
#例: [{"role": "system", "content": "Hello, how are you?"}, {"role": "user", "content": "I'm good. What are you up to?"}]
#role は assistant:GPTによる返信 user:ユーザーとして対話 system:システムプロンプト が使える