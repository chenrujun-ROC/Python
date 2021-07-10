# 抓取 PTT 電影板的網頁原始碼 (HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/Stock/index.html"
# 建立一個 Request 物件. 附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)
