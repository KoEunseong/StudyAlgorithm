import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

data.sort()

answer = 0
isAnswer = False
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum = data[i] + data[j] + data[k]
            if sum > answer and sum <= M :
                answer = sum

print(answer)
