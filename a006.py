import math

a,b,c = map(int,input("a,b,c for ax2+bx+c=0: ").strip().split())
try:
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
    if x1 == x2:
        print("Two same roots x="+x1)
    else:
        print("Two different roots x1="+x1+",x2="+x2)
except:
    print("No real root")