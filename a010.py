import math

# cin = 100000000
cin = int(input("num: "))
# 質數範圍：2~cin
ls = [2]
# 建構質數範圍列表
for i in range(3, cin+1):
    ls.append(i)
# 找第一個未被刪掉的數字n=ls[0]，刪除其2~cin//n倍
# 找下一個數字ls[1]，刪除其倍數，當ls[0]*2>cin就可以停止
order_of_prime = 0
while ls[order_of_prime]*2 < cin:
    for i in range(2,cin//ls[0]+1):
        if ls[order_of_prime]*i in ls:
            ls.remove(ls[order_of_prime]*i)  
    order_of_prime += 1

# 找cin質因數
factor = []
for i in range(len(ls)):
    if cin//ls[i] == 0:
        factor.append(i)
# 質因數的次方
for i in range(len(factor)):
    power = 0
    while cin//factor[i] ==0:
        power += 1
    if power != 0:
        print(str(ls[i])+'^'+str(power),end='')
    else:
        print(str(s),end='')
    if i+1 != len(factor):
        print(" * ",end='')
print()
# //判斷要不要印出”*”， 次方=1就不用印"^"了

# 20 -> 2^2 * 5
# 17 -> 17
# 999997 -> 757 * 1321

# a1 = 2
# a2 = 5
# p1 =2
# print("%d^%d * %d" %(a1,p1,a2))