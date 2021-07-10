# # 網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw/"               # 台灣大學網址
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")    # 取得台灣大學網站的原始碼 (HTML)
# print(data)

# 網路連線
import urllib.request as request
import json
src="https://www.tpex.org.tw/openapi/swagger.json"               
with request.urlopen(src) as response:
    data=json.load(response)    
print(data)
