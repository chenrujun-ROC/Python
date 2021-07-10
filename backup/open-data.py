# # 網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw/"               # 台灣大學網址
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")    # 取得台灣大學網站的原始碼 (HTML)
# print(data)

# 網路連線
from types import ClassMethodDescriptorType
import urllib.request as request
import json
src="https://data.tycg.gov.tw/api/v1/rest/datastore/f4ece141-4044-45bf-8a2d-2d1f1171dd74?format=json%22"               
with request.urlopen(src) as response:
    data=json.load(response)
# 將公司名稱列表出來
clist=data["result"]["records"]
with open("data.txt", mode="w", encoding="utf-8") as file:
    for company in clist:
        file.write("傳真號碼: "+company["傳真"]+" 機關名稱: "+company["機關名稱"]+"\n")
