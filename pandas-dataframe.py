# 載入 pandas 模組
from os import sep
import  pandas as pd
# 資料索引: DataFrame(字典, index=索引列表)
data=pd.DataFrame({
    "name":["Amy", "bob", "charles"],
    "salary":[30000, 50000, 40000]
},index=["a", "b", "c"])
print(data)
print("============")

# # 觀察資料
# print("資料數量",data.size)
# print("資料形狀(列)(攔)",data.shape)
# print("資料索引",data.index)

# 取得列 (Row/橫向) 的 Series 資料: 根據順序 根據索引
# print("取得第二列", data.iloc[1], sep="\n")           # 取得第 二 列
# print("============")
# print("取得第c列", data.loc["c"], sep="\n")           # 取得第 三 列

# 取得欄 (Column/直向) 的 Series 資料: 根據順欄位名稱
# print("取得 name 欄位", data["name"], sep="\n")         # 取得 name 欄
# print("取得 salary 欄位", data["salary"], sep="\n")     # 取得 salary 欄

# names=data["name"]
# print("把 name 全部轉大寫", names.str.upper(),sep="\n")

# # 計算薪水的平均值
# salaries=data["salary"]
# print("薪水的平均值", salaries.mean

# 建立新的欄位
data["revenue"]=[500000, 400000, 300000]                # data[新欄位的名稱]=列表
data["rank"]=pd.Series([3, 6, 1], index=["a", "b", "c"])# data[新欄位名稱]=Series 的資料
data["cp"]=data["revenue"]/data["salary"]  
print(data)
