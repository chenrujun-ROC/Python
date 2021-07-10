# 隨機模組
import random

# 隨機選取
data=random.choice([1,5,6,10,20])
print(data)

# 隨機選取(多筆資料)(3)
data=random.sample([1,5,6,10,20], 3)
print(data)

# 隨機調換順序 (就是洗牌的概念)
data=[1,5,8,20]
random.shuffle(data)
print(data)

# 隨機取得亂數
data=random.random()                # 0.0-1.0 之間的隨機亂數
print(data)
data=random.uniform(0.0,1.0)        # 0.0-1.0 之間的隨機亂數
print(data)
data=random.uniform(60,100)         # 60-100 之間的隨機亂數
print(data)

# 取得常態分配亂數
# 平均數 100,標準差 10, 得到的資料多數在 90-110 之間
data=random.normalvariate(100,10)
print(data)

# 平均數 0,標準差 5, 得到的資料多數在 -5-5 之間
data=random.normalvariate(0,5)
print(data)

# 統計模組
# 平均數
import statistics as stat
data=stat.mean([1,2,3,4,5,8,10])
print(data)

# 中位數
import statistics as stat
data=stat.median([1,2,3,4,5,8,10])
print(data)

# 標準差
import statistics as stat
data=stat.stdev([1,2,3,4,5,8,10])
print(data)
