import sys

N = int(input())

data = []
for _ in range(N):
    n1,n2 = map(int,sys.stdin.readline().split())
    data.append((n1, n2))

data.sort(key=lambda x: (x[1], x[0]) )
for item in data:
    print(item[0],item[1])
