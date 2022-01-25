#!/usr/bin/python3
# -*- coding: utf-8 -*-

# h = int(input("高度h = "))
# w = int(input("寬度w = "))
# d = int(input("長度d = "))

path = "./"
f_in = open(path_in, "r")
lines = f_in.readlines()
for line in lines:
    pass
f_in.close()

sur = 2*(h*w + w*d + d*h)
vol = h*w*d

print(sur, vol, end=" ")
print()