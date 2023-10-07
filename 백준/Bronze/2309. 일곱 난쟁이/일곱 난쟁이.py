import sys

data = [int(sys.stdin.readline()) for _ in range(9)]

data.sort()

others = sum(data) - 100


for i in range(9):
    for j in range(i + 1, 9):
        if data[i] + data[j] == others:
            p1, p2 = data[i], data[j]
            break

data.remove(p1)
data.remove(p2)
            
for item in data:
    print(item)
