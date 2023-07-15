import sys

A, B, V = map(int,sys.stdin.readline().split())

day = 0
loc = 0
gap = A - B 

if (V - A) % gap == 0:
    day = (V - A) // gap + 1
else :
    day = (V - A) // gap + 2


print(day)