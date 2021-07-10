# 有序可變動列表 List
grades=[12,60,15,70,90]
grades[0]=55                #把55放到列表中的第一個位置
grades[1:4]=[]              #連續刪除列表中從編號1到編號4(不包括) 的資料
grades=grades+[12,33]       #把資料加入列表中
print(grades)

length=len(grades)          #取得列表的長度 len(列表資料)
print(length)

data=[[3,4,5],[5,7,8]]
data[0][0:2]=[5,5,5]
print(data[0])
# 有序列不可變動列表 Tuple
data=(3,4,5)
#data[0]=5                   #錯誤: Tuple資料不可以變動('tuple' object does not support item assignment)
print(data)