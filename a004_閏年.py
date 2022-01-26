def leap_year(year):
    """閏年規則: 西元年被4整除且不被100整除，或被400整除者即為閏年
    非4的倍數（1st多），平年。
    （剩下的都是4的倍數）
    非100的倍數（2nd多），闰年，400的倍數，閏年。
    100的倍數，非400的倍數，平年。
    """
    # 資料中，不是4的倍數比較多，所以先判斷這個，大部分的case在這個if就解決了，不用走到elif
    if (year % 4 != 0): # 非4的倍數为平年
        leap = False
    # 剩下的都是4的倍數
    elif (year % 100 != 0) or (year % 400 == 0):
        leap = True
    else:
        leap = False
    return leap

def ans(leap):
    if leap:
        print("閏年")
    else:
        print("平年")

while True:
    try:
        year = int(input())
        leap = leap_year(year)
        ans(leap)
    except:
        break
##################################################
"""
while True:
    try:
        cin = int(input())
        if (cin % 4 == 0 and cin % 100 != 0):
            print("閏年")
        elif cin % 400 == 0:
            print("閏年")
        else:
            print("平年")
    except:
        break
"""
##################################################
'''
import sys
lines=[]
while True:
    aLine=sys.stdin.readline()
    if aLine=="":
        break
    lines.append(aLine)
print(lines)
'''
