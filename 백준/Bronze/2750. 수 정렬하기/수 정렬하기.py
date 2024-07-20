import sys

N = int(input())

arr = []
for i in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)
arr.sort()
for item in arr:
    print(item)
