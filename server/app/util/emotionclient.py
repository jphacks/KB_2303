#google natural languageの感情分析APIを叩くクライアント
#環境変数にGOOGLE_APPLICATION_CREDENTIALSを設定しておくこと
#https://cloud.google.com/natural-language/docs/analyzing-sentiment?hl=ja
from google.cloud import language_v1

# APIKEYファイルを設定(予めGCPで認証ファイルを作成しておく必要がある)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./thiscode-403012-a9a35deaf88d.json"

client = language_v1.LanguageServiceClient()

text_content = '今日は天気が良い'
# Available types: PLAIN_TEXT, HTML
type_ = language_v1.Document.Type.PLAIN_TEXT
language = "ja"
document = {"content": text_content, "type_": type_, "language": language}

# Available values: NONE, UTF8, UTF16, UTF32
encoding_type = language_v1.EncodingType.UTF8

response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
# Get sentiment for all sentences in the document
score = []
magnitude = []
for sentence in response.sentences:
    print( 'score:{}'.format(sentence.sentiment.score) )
    print( 'magniture:{}'.format(sentence.sentiment.magnitude ) )