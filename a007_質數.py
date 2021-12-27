# 減少記憶體的做法：
# http://web.ntnu.edu.tw/~algo/Prime.html
# list用二進制的T、F來儲存
# 欲刪掉質數 i 的倍數之時，早已刪掉「小於 i 的質數、其倍數」倍了
# 直接刪掉「大於等於 i 的質數、其倍數」倍。
# 一個合數 x ，必定有一個小於等於 sqrt(x) 的質因數。
# 所有小於等於 sqrt(x) 的質數，刪掉這些質數的倍數，就能刪掉所有合數了。
# for (int k=(20000000-1)/i, j=i*k; k>=i; k--, j-=i)k是倍率，j是質數i的倍數。
# 由大到小判斷，當prime[k]成立時，
# k才能涵蓋所有「大於等於i的質數、其倍數」倍。

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