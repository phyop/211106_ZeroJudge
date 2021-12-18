cin = input()
l = len(cin)
i = 0
ls = []
for i in range(l):
    a = chr(ord(cin[i])-7)
    ls.append(a)
    i = i + 1
print(''.join(ls))


# $ https://www.itread01.com/content/1547965466.html
# $ str轉換為list
# <list> = <str>.split(<separator>)
# $ list轉換為str
# <str> = <separator>.join(<list>)
# $ extend
# a=[1,2,3]
# b=[9,8,7]
# test=a.extend(b)
# print(a)        #[1, 2, 3, 9, 8, 7]
# print(test)     #None
# $ ord('r') -> 114 ; chr(97) -> a
