# 載入 pandas 模組
import pandas as pd

# 資料索引
data=pd.Series([5, 4, -2, 3, 7], index=["a", "b", "c", "d", "e"])
print(data)

# 觀察資料
print("資料型態", data.dtype)
print("資料數量", data.size)
print("資料索引", data.index)
print(data[2], data[0])
print(data["e"], data["d"])

# 數字運算: 基本, 統計, 順序
print("最大值", data.max())
print("最小值", data.min())
print("總和", data.sum())
print("標準差", data.std())
print("平均值", data.mean())
print("中位數", data.median())
print("最大的三個數", data.nlargest(3),sep="\n")
print("最小的三個數", data.nsmallest(3),sep="\n")

data=pd.Series(["您好", "Python", "Pandas"])
# 
# 字串運算: 基本, 串接, 搜尋, 取代
print(data.str.lower())                 #全部變小寫 (中文不受影響)
print(data.str.upper())                 #全部變大寫 (中文不受影響)
print(data.str.len())                   #算出每個字串的長度
print(data.str.cat(sep="/"))            #把字串串接起來, 可以自訂串接的符號
print(data.str.contains("P"))           #判斷每個字串是否包含特定的字元
print(data.str.replace("您好", "Hello"))#重新定義字串   