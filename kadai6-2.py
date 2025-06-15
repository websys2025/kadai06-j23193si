import requests

API_URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/120000.json"

#気象庁 天気予報データ API　　（今回は千葉県の天気予報データを取得）
#概要：日本の天気予報情報をJSON形式で取得できるAPI

#endpoint：https://www.jma.go.jp/bosai/forecast/data/forecast/120000.json
#使い方：地域コードを指定し天気予報情報を取得（今回は　千葉県：120000）

response = requests.get(API_URL)
data = response.json()
print(data)