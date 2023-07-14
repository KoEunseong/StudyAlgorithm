import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
new_data = [] 
M = max(data)

for i in data:
    new_data.append(i / M * 100)
print(sum(new_data) / N)