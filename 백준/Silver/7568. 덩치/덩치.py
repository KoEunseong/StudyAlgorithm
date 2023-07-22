import sys

N = int(input())
people = []
for i in range(N):
    w,h = map(int, sys.stdin.readline().split())
    people.append((w,h))

for item in people:
    rank = 0
    for i in people:
        if item[0] < i[0] and item[1] < i[1]:
            rank += 1
    
    print(rank + 1,end=' ')