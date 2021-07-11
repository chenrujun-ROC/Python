# 載入 pandas 模組
from os import sep
import  pandas as pd
# 資料索引: DataFrame(字典, index=索引列表)
data=pd.DataFrame({
    "name":["Amy", "bob", "charles"],
    "salary":[3000, 50000, 40000]
},index=["a", "b", "c"])
print(data)
print("============")

# 觀察資料
print("資料數量",data.size)
print("資料形狀(列)(攔)",data.shape)
print("資料索引",data.index)

# 取得列 (Row/橫向) 的 Series 資料: 根據順序 根據索引
print("根據第二列", data.iloc[1], sep="\n")   # 取得第二列

# 取得欄 (Column/直向) 的 Series 資料: 根據順欄位名稱