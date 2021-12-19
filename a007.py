import math

# cin = 2147483647
cin = 67483647
# 質數範圍：2~sqrt(cin) 
ls = [2]
mid = int(math.sqrt(cin))
# 建構質數範圍列表
for i in range(3, mid):
    ls.append(i)
# 找第一個未被刪掉的數字n=ls[0]，刪除其2~mid//n倍
# 找下一個數字ls[1]，刪除其倍數，當ls[0]*2>mid就可以停止
order_of_prime = 0
while ls[order_of_prime]*2 < mid:
    for i in range(2,mid//ls[0]+1):
        if ls[order_of_prime]*i in ls:
            ls.remove(ls[order_of_prime]*i)  
    order_of_prime += 1
# print(len(ls))
# 1000以內的質數有168個

while True:
    try:
        cin_real = int(input())
        if cin_real in ls:
            print("質數")
        else:
            print("非質數")
    except:
        break