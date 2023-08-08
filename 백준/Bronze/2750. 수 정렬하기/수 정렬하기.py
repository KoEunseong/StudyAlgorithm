import sys

N = int(input())
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))
    
for i in range(N - 1, 0, -1):
    for j in range(i):
        if data[j] > data[j + 1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp
        
for i in data:
    print(i)