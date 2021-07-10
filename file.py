# 儲存檔案
# file=open("data.txt",mode="w",encoding="utf-8")             # 開啟
# file.write("Hello File\nSecond File")                       # 操作
# file.close()                                                # 關閉
# 使用with開啟
# with open("data.txt",mode="w",encoding="utf-8")as file:        # 開啟且自動關閉
#     file.write("5\n3")                              # 操作

# 讀取檔案
# with open("data.txt",mode="r",encoding="utf-8")as file:
#     data=file.read()
# print(data)
# 把資料中的數字資料, 一行一行讀取出來, 並計算總合
# sum=0
# with open("data.txt", mode="r", encoding="utf-8")as file:
#     for line in file:               # 一行一行的讀取
#         sum+=int(line)
print(sum)

# 使用 JSON 格式讀取, 複寫檔案
import json
# 從檔案中讀取 JSON 資料, 放入變數 data 裡面
with open("config.json", mode="r", encoding="utf-8") as file:
    data=json.load(file)
print(data)                         # data 是一個字典資料
print(type(data))
print("name", data["name"])
print("version", data["version"])
data["name"]="New name"
# 把最新的資料複寫回檔案中
with open("config.json", mode="w", encoding="utf-8") as file:
    json.dump(data, file)