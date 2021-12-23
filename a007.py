import math

cin = 10000
ls = []
# 建構質數範圍列表，質數範圍：2~cin
for i in range(2, cin+1):
    ls.append(i)
# 找第一個未被刪掉的數字n=ls[0]，刪除其倍數，i.e 2~cin//n倍
# 找下一個數字ls[0 + count]，刪除其倍數，i.e 2~cin//ls[0 + count]倍
# 直到ls[-1]
order_of_prime = 0
while ls[order_of_prime] != ls[-1]: # 直到ls[-1]
    for i in range(2,cin//ls[order_of_prime]+1): # 2~cin//n倍
        if ls[order_of_prime]*i in ls: # 刪除其倍數
            ls.remove(ls[order_of_prime]*i)  
    order_of_prime += 1 

while True:
    try:
        cin_real = int(input())
        if cin_real in ls:
            print("質數")
        else:
            print("非質數")
    except:
        break