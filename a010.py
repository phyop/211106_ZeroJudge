import math

cin = int(input("Num: "))
# 質數範圍：2~sqrt(x) 
ls = [2]
mid = int(math.sqrt(cin))
# 建構質數表
for i in range(3, mid):
    ls.append(i)
print(ls)
# 刪除第1個質數的倍數
for i in ls:
    if i % ls[0] == 0:
        ls.remove(i)
# 找第一個未被刪掉的數字n=ls[0]，刪除其2~mid//n倍
for i in range(2,mid//ls[0]):
    ls.remove(ls[0]*i)

print(ls)



# 刪掉 2 的倍數。
# 找下一個未被刪掉的數字，
# 找到 3 ，
# 刪掉 3 的倍數。
# 找下一個未被刪掉的數字。
# //判斷要不要印出”*”， 次方=1就不用印"^"了
# print(str(s)+'^'+str(n),end='') 輸出時記得設print()為不要換行

# 20 -> 2^2 * 5
# 17 -> 17
# 999997 -> 757 * 1321
