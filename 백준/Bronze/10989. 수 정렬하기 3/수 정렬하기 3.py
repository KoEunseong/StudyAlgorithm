import sys
N = int(sys.stdin.readline())
data = {}

for _ in range(N):
    num = int(sys.stdin.readline())
    if num in data:
        data[num] += 1
    else :
        data[num] = 1
    
data = sorted(data.items())

for item in data:
    for i in range(item[1]):
        print(item[0])