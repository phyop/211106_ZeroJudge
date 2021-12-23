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

cin_real = int(input())
# 找cin質因數
factor = []
for i in range(len(ls)):
    if cin_real % ls[i] == 0:
        factor.append(ls[i])
# 質因數的次方
for i in range(len(factor)):
    power = 0
    while cin_real % factor[i] == 0:
        cin_real //= factor[i]
        power += 1
    if power = 0:
        continue
    elif power = 1:
        print(str(ls[i]),end='')
    else:
        print(str(ls[i])+'^'+str(power),end='')
    if i+1 != len(factor):
        print(' * ')
print()
# //判斷要不要印出”*”， 次方=1就不用印"^"了

# 20 -> 2^2 * 5
# 17 -> 17
# 999997 -> 757 * 1321

# a1 = 2
# a2 = 5
# p1 =2
# print("%d^%d * %d" %(a1,p1,a2))