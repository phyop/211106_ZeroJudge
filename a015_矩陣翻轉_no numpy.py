while True:
    try:
        ori_array = []
        flip_array = []
        ori_r, ori_c = map(int, input().strip().split())
        flip_r = ori_c
        flip_c = ori_r
        
        for _ in range(ori_r):
            # 每一row就建一個list
            ori_ri = list(map(int, input().strip().split()))
            # 用一個list，把每一個row都裝進來，就是array了
            ori_array.append(ori_ri)
        
        for i in range(flip_r):
            # flip有幾row，就先建幾個空list
            flip_array.append([])
            for j in range(flip_c):
                # 先對第i個row，把值填完
                flip_array[i].append(ori_array[j][i])
        
        for r in range(flip_r):
            # *就是解包的意思
            print(*flip_array[r])
    except:
        break

# for r in range(flip_r):
#     if r!= 0:
#         print()
#     for c in range(flip_c):
#         # 不知道為什麼，加了「end=」，在某些compiler輸出就啥都沒有，或最後一行沒有
#         print(flip_array[r][c], end=' ')
#         # from sys import stdout
#         # stdout.write(flip_array[r][c]+' ')

# 3 4
# 3 5 6 7
# 1 3 4 66
# 3 5 6 77