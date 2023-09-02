import sys
sys.setrecursionlimit(10*6)

N = int(input())
data = []
for _ in range(N):
    n1, n2 = map(int, sys.stdin.readline().split())
    data.append((n1, n2))

data.sort(key = lambda x : (x[1], x[0]))
# print(data)


running = 0
answer = 0
for item in data:
    if item[0] < running : 
        continue
    running = item[1]
    answer += 1

print(answer)