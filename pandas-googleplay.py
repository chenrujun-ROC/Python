import pandas as pd
# 讀取資料
data=pd.read_csv("googleplaystore.csv")     # 把 csv 格式的檔案讀取成一個 DataFrame
# 觀察資料
# print("資料數量", data.shape)
# print("資料欄位", data.columns)
# print("=========================")

# 分析資料:評分的各種統計數據
condition=data["Rating"]<=5
data=data[condition]
print("平均數", data["Rating"].mean())
print("中位數", data["Rating"].median())
print("取得前100個應用程式的平均", data["Rating"].nlargest(100).mean())


# 分析資料:安裝數量的各種統計數據
# 基於資料的應用:關鍵字搜尋應用程式名稱