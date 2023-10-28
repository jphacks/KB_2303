#google natural languageの感情分析APIを叩くクライアント
#環境変数にGOOGLE_APPLICATION_CREDENTIALSを設定しておくこと
#https://cloud.google.com/natural-language/docs/analyzing-sentiment?hl=ja
from google.cloud import language_v1
import  os
# APIKEYファイルを設定(予めGCPで認証ファイルを作成しておく必要がある)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../../thiscode-403012-a9a35deaf88d.json"


#scoreは０が平常でプラスの値がポジティブ、マイナスの値がネガティブ
#magnitudeは確度を表す。感情表現が多いほど大きくなる。感情表現がないと0になる
#基本的にscoreのみ使えばいいと思う

def emotionscore(text):
    client = language_v1.LanguageServiceClient()
    text_content = text
    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "ja"
    document = {"content": text_content, "type_": type_, "language": language}
    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get sentiment for all sentences in the document
    #print(response)
    score = []
    magnitude = []
    for sentence in response.sentences:
        score.append(sentence.sentiment.score)
        magnitude.append(sentence.sentiment.magnitude)
    #print("score",score)
    #print("magnitude",magnitude)
    return  sum(score)/len(score),sum(magnitude)/len(magnitude)
  
  
  
if __name__ == "__main__":
  emotion=emotionscore(input("テキストを入力してください: "))
  print(emotion)