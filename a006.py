import math

# a,b,c = map(int,input("a,b,c for ax2+bx+c=0: ").strip().split())
a,b,c = map(int,input().strip().split())
try:
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    if x1 != x2:
        print("Two different roots x1=%d , x2=%d" %(x1,x2))
    else:
        print("Two same roots x=%d" %(x1))
except:
    print("No real root")