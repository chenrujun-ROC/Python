# 載入 pandas 模組
from os import sep
import  pandas as pd

# 篩選練習 - Series
# data=pd.Series([30, 15, 20])
# condition=data>18
# print(condition)
# filteredData=data[condition]
# print(filteredData)

# data=pd.Series(["您好", "Python", "Pandas"])
# condition=data.str.contains("P")
# print(condition)
# filteredData=data[condition]
# print(filteredData)

# 篩選練習 - DataFrame
data=pd.DataFrame({
    "name":["Amy", "bob", "charles"],
    "salary":[30000, 50000, 40000]
})
# print(data)
condition=data["salary"]>=40000
print(condition)
filteredData=data[condition]
print(filteredData)

condition=data["name"]=="Amy"
print(condition)
filteredData=data[condition]
print(filteredData)
