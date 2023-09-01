import sys

N, K = map(int , sys.stdin.readline().split())

data = [0 for _ in range(N)]
for i in range(N - 1, 0 - 1 , -1):
    data[i] = int(sys.stdin.readline())

answer = 0
rest = K
for item in data :
    answer += rest // item
    rest = rest % item
    
print(answer)