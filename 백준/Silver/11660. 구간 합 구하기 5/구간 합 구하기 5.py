import sys

N,M = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

question = []
sum_data = [[0 for _ in range(N)] for _ in range(N)]


sum = 0
for i in range(N):
    sum += data[0][i]
    sum_data[0][i] = sum


sum = 0
for i in range(N):
    sum += data[i][0]
    sum_data[i][0] = sum

for i in range(1,N):
    for j in range(1,N):
        sum_data[i][j] = sum_data[i - 1][j] + sum_data[i][j - 1] - sum_data[i - 1][j - 1] + data[i][j]

for _ in range(M):
    
    n1, n2, n3, n4 = map(lambda x : int(x) - 1, sys.stdin.readline().split()) # 1 1 2 3
    if n2 == 0:
        a = 0
    else :
        a = sum_data[n3][n2 - 1]
    if n1 == 0:
        b = 0
    else :
        b = sum_data[n1 - 1][n4]
    
    if a == 0 or b == 0:
        c = 0
    else :        
        c = sum_data[n1 - 1][n2 - 1]
    
    answer = sum_data[n3][n4] - a - b + c
    print(answer)
    
    

