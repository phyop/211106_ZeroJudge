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
