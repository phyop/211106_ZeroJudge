import numpy as np

m, n = map(int, input().strip().split())
row = []

for i in range(m):
    r = list(map(int, input().strip().split()))
    row.append(r)
array = np.array(row)

zero_arr = np.zeros((n,m))
for i in range(m):
    for j in range(n):
        zero_arr[i][j] = array[j][i]
print(array)

# [None] * 10
# [None for _ in range(10)]
# [元素要放什麽值 for _ in range(做幾次)]
# timeit --- 测量小代码片段的执行时间
# timeit("for _ in range(10): a.append(None)", setup="a=[]")
# timeit("for _ in range(10): a.append(None)", 在這之前的條件")
# 使用迴圈是最慢的方法，需要 842 毫秒才能完成一百萬次迭代
