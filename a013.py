# 減法組合只有六種情況：
dic_m = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
# 加法組合
dic_p = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def combi2(s):
    for i in range(len(s)-1):
        combine = s[i]+s[i+1]
        if combine in dic_m.keys():
            pass

def ro2nu(s1,s2):
    """ I I -> 0; MM II -> 1998 """
    if s1 == s2:
        return 'ZERO'
    
        

def nu2ro(num):
    """ 0 -> ZERO, 1998 -> MCMXCVIII """
    pass


while input() != '#':
    try:
        s1,s2 = input().split()
        nu = ro2nu(s1,s2) # number after minus
        ro = nu2ro(nu)
        print(ro)
    except:
        break


"""
右邊較小，表示右加。
左邊較小，表示左減。
右加數字不能超過3位 -> 比如14寫成XIV，而非XIIII。
左減不能跨越一個位數 -> 比如，99不可以用IC表示，而是用XCIX表示。
左減數字不能超過1位 -> 比如8寫成VIII，而非IIX。
https://king39461.pixnet.net/blog/post/395774992

通常情況下，羅馬數字中小的數字在大的數字的右邊。但也存在特例，例如 4和9。
這個特殊的規則只適用於以下六種情況：
I 可以放在 V (5) 和 X (10) 的左邊，來表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左邊，來表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左邊，來表示 400 和 900。
"MCMXCIV"輸出: 1994: M = 1000, CM = 900, XC = 90, IV = 4
https://ppfocus.com/0/fa55b9db2.html

罗马数字转换工具:
https://zh.romannumerals.guide/MCMXCVIII

I I -> (1) - (1) -> ZERO
MM II -> (1000+1000) - (1+1) -> MCMXCVIII 
I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)
(1+1+1+5+100-10+1000-100+1000) = 1998 -> +++++-+-+ -> 111110101
(1000-100+1000-10+100+5+1+1+1) = 1998 -> +-+-+++++ -> 101011111

1998
-> M 先給大於value的最小rome；如果沒有value大於最大rome，則給最大rome(M)
-> MM 判斷當前rome與value的差距（2）,尋找
"""