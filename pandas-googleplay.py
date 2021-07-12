import pandas as pd
# 讀取資料
data=pd.read_csv("googleplaystore.csv")     # 把 csv 格式的檔案讀取成一個 DataFrame
# 觀察資料
# print("資料數量", data.shape)
print("資料欄位", data.columns)
# print("=========================")

# 分析資料:評分的各種統計數據
# condition=data["Rating"]<=5
# data=data[condition]
# print("平均數", data["Rating"].mean())
# print("中位數", data["Rating"].median())
# print("取得前100個應用程式的平均", data["Rating"].nlargest(1000).mean())

# 分析資料:安裝數量的各種統計數據
condition=data["Type"]="Paid"
data=data[condition]
print(data["Type"])
data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[+,]","").replace("Free",""))
print("平均數", data["Installs"].mean())
condition=data["Installs"]>100000
print("安裝數量大於 100000 的應用程式的有幾個", data[condition].shape[0])
# 基於資料的應用:關鍵字搜尋應用程式名稱