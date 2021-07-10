# 定義函式
# 函式內部的程式碼, 若是沒有做函式呼叫, 就不會執行
def multiply(n1,n2):
    print(n1*n2)
    return n1*n2
# 呼叫函式
value=multiply(5,5)+multiply(5,10)
print(value)

# 程式的包裝
def caculate(n1,n2):
    sum=0
    for n in range(n1,n2+1):
        sum=sum+n
    print(sum)
n1=int(input("輸入一個正整數: "))
n2=int(input("輸入一個正整數: "))
caculate(n1,n2)