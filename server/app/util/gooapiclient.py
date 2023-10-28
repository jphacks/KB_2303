#gooapiの日時抽出、名前抽出のAPIを使うための関数
#環境変数にGOO_API_IDを設定しておくこと
import requests
import json
from env import get_env
from datetime import datetime
from dateutil.parser import parse
#DATETIME型で返す。日時が含まれていない場合はNoneを返す
def gooclient_time(text):
  requesttext=text
  requestjson={"app_id":get_env("GOO_API_ID", ""),"sentence":requesttext}
  response=requests.post("https://labs.goo.ne.jp/api/chrono",json=requestjson)
  if response.status_code != 200:
    print("error")
    return None
  if response.json()["datetime_list"] is None:
    return None
  if len(response.json()["datetime_list"])==2:
    return datetime.strptime( response.json()["datetime_list"][1][1], '%Y-%m-%dT%H')#YYYY-mm-ddTHH:MM:SSの
  else:
    return datetime.strptime(response.json()["datetime_list"][0],'%Y-%m-%dT%H')#YYYY-mm-ddTHH:MM:SSの
  return None
  #print(response.json())
#gooラボAPiを使って名前を抽出する

#フルネームを文字列で返す。フルネームではない場合やそもそも名前が含まれていない場合はNoneを返す
def gooclient_name(text):
  requesttext=text
  requestjson={"app_id":get_env("GOO_API_ID", ""),"sentence":requesttext}
  response=requests.post("https://labs.goo.ne.jp/api/slot",json=requestjson)
  #print(response.json())
  if response.status_code != 200:
    print("error")
    return "APIError"
  if len(response.json()["slots"]["name"][0])!=2:
    return None
  else:
    return response.json()["slots"]["name"][0]["surname"]+response.json()["slots"]["name"][0]["given_name"]

if __name__ == "__main__":
  responsejson=gooclient_time("相談の件ですが明後日の3時から面談を入れられますがいかが致しましょうか")#時刻のサンプル
  print(responsejson,type(responsejson))
  responsejson=gooclient_name("伊藤太郎です。よろしくお願いします")
  print(responsejson,type(responsejson))