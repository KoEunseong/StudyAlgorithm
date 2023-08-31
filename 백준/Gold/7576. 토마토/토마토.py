import sys
sys.setrecursionlimit(10**6)
from collections import deque
import time

N, M = map(int , sys.stdin.readline().split()) # 6 4
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

data = []
for _ in range(M):
    line = list(map(int , sys.stdin.readline().split()))
    data.append(line)

visited = [[False for _ in range(N)] for _ in range(M)]            


def BFS(n1, n2):
    global visit_count
    que = deque()
    ripedTomato = []
    visited[n1][n2] = True
    visit_count += 1
    que.append((n1, n2))
    
    while que :
        num = que.popleft()
        for i in range(4):
            x = num[0] + dx[i]
            y = num[1] + dy[i]
            
            if x >=0 and y >=0 and x < M and y < N :
                # if data[x][y] == 0 and not visited[x][y]:
                if data[x][y] == 0:
                    data[x][y] = 1
                    ripedTomato.append((x,y))
                    # visited[x][y] = True
                    # visit_count += 1
                # elif data[x][y] == -1 and not visited[x][y]:
                #     visited[x][y] = True
                #     visit_count += 1
    return ripedTomato

answer = 0
visit_count = 0

for i in range(M):
        for j in range(N):
            # if data[i][j] == 1 or data[i][j] == -1:
            if data[i][j] == -1:
                visit_count += 1
                
ripedTomato = []

for i in range(M):
    for j in range(N):      
        if data[i][j] == 1 and not visited[i][j]:
            ripedTomato.append((i, j)) 

while visit_count < N * M and len(ripedTomato) != 0:
    # ripedTomato = []
    newMato = []
    
        
    # ripedTomato = []
    # for i in range(M):
    #     for j in range(N):      
    #         if data[i][j] == 1 and not visited[i][j]:
    #             ripedTomato.append((i, j)) # 새로 익은 토마토 위치 찾기
    
    for item in ripedTomato:
        n1 , n2 = item
        newMato.extend(BFS(n1, n2))
    # print(newMato)
    # print(data)
    # print(visit_count)
    # time.sleep(5)
    ripedTomato = newMato
    answer += 1
        
# print(data) 
isTrue = True
for i in range(M):
    for j in range(N):
        if data[i][j] == 0 :
            isTrue = False
            break
if isTrue :
    print(answer - 1)
else :
    print(-1)
