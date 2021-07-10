#集合的運算
set1={3,4,5}
set2={4,5,6,7}
print(3 in set1)
print(3 not in set1)
print(10 in set1)
print(10 not in set1)
# 交集&: 取兩個集合中, 相同的資料
set3=set1&set2
print(set3)
# 聯集|: 取兩個集合中的所有資料, 但不重複取
set4=set1|set2
print(set4)
# 差集-: 從set1中, 減去和set2重疊的部分
set5=set1-set2
print(set5)
# 反交集^: 取兩個集合中, 不重疊的部分
set6=set1^set2
print(set6)
# set(字串)
set7=set("hello")
print(set7)
print("h" in set7)
print("H" in set7)
print("h" not in set7)
print("H" not in set7)
# 字典的運算: key-value 配對
dic={"apple":"蘋果","bug":"蟲蟲"}
print(dic["apple"])
dic["apple"]="小蘋果"
print(dic["apple"])
# 判斷key是否存在
print("apple" in dic)
print(dic)
# 刪除字典中的鍵值對 (key-value pair)
del dic["apple"]
print(dic)
# 從列表資料產生字典
dic={x:x*2 for x in [3,4,5]}
print(dic)