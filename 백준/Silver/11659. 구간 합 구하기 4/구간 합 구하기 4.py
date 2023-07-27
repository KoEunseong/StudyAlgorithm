import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

sum_data = [0]
sum = 0
for i in data:
    sum += i
    sum_data.append(sum)

for _ in range(M):
    n1 , n2 = map(int, sys.stdin.readline().split())
    print(sum_data[n2] - sum_data[n1 - 1])