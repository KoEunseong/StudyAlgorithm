import sys
sys.setrecursionlimit(10**7)
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N = int(input())
data = []
visited = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N):
    line = list(map(int , input()))
    data.append(line)


def BFS(n1, n2):
    members = 0
    que = deque()
    
    que.append((n1, n2))
    
    if data[n1][n2] == 1:
        members += 1
        visited[n1][n2] = True
    
    while que :
        now = que.popleft()
        for i in range(4): # up , down, left, right
            x = now[0] + dx[i]
            y = now[1] + dy[i]
            
            if x >= 0 and y >= 0 and x < N and y < N:
                if data[x][y] != 0 and not visited[x][y]:
                    members += 1
                    visited[x][y] = True
                    que.append((x, y))
    
    return members



answer = []
for i in range(N):
    for j in range(N):
        if data[i][j] != 0 and not visited[i][j]:
        # if not visited[i][j]:
            num = BFS(i, j)
            if num != 0:
                answer.append(num)

answer.sort()
print(len(answer))
for item in answer :
    print(item)

# print(data)
# print(visited)
