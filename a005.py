t = int(input("how many series: "))
for i in range(t):
    # https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
    l = list(map(int,input("\nseries : ").strip().split()))
    d = l[3]-l[2]
    m = l[3]//l[2]
    # 如果是等差，那越後面的相鄰數值，越不可能整除，所以藉由判別是不是整除，來確定等比還是等差
    # 最小的等差 1234
    # 最小的等比 1248
    if l[3]%l[2] != 0 : # 那就是等差
        l.append(l[3]+d)
        # https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
    else: # 等比
        l.append(l[3]*m)
    print(*l)



"""
https://reurl.cc/n5aYYX
read([size])
從檔案當前位置起讀取size個位元組，若無引數size，則表示讀取至檔案結束為止，它範圍為字串物件
readline()
每次讀出一行內容，所以，讀取時佔用記憶體小，比較適合大檔案，該方法返回一個字串物件
readlines()
讀取整個檔案所有行，儲存在一個列表(list)變數中，每行作為一個元素，但讀取大檔案會比較佔記憶體
"""