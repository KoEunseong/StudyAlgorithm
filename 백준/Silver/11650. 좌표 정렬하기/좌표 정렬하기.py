import sys

N = int(input())

data = []
for _ in range(N):
    n1,n2 = map(int,sys.stdin.readline().split())
    data.append((n1, n2))

data.sort()
for item in data:
    print(item[0],item[1])
