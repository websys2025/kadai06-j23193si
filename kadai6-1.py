import requests

APP_ID = "4dee867a44e3cb5a92bfbc68331e9d5534d3393d"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {   #企業のワーク・ライフ・バランスに関する調査 
    "appId": APP_ID,
    "lang":"J",
    "statsDataId":"0003346052",
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":1,
    "replaceSpChars":0
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)