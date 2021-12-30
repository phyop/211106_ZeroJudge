m, n = map(int, input().strip().split())
row = []
# 3 4
# 3 5 6 7
# 1 3 4 66
# 3 5 6 77

for i in range(m):
    r = list(map(int, input().strip().split()))
    row.append(r)
# [[3, 5, 6, 7], [1, 3, 4, 66], [3, 5, 6, 77]]

zero_arr = np.zeros((n,m))
for i in range(n):
    for j in range(m):
        zero_arr[i][j] = array[j][i]
