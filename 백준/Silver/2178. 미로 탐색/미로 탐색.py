import sys
from collections import deque

sys.setrecursionlimit(10**7)

N, M = map(int , sys.stdin.readline().split())

data = [ [0 for _ in range(M)] for _ in range(N)]


visited = [[False for _ in range(M)] for _ in range(N)]
dx = [0,0, 1,-1]
dy = [1, -1, 0,0]

for i in range(N):
    line = sys.stdin.readline()
    for j in range(M) :
        data[i][j] = int(line[j])

def BFS():
    
    que = deque()
    que.append((0,0))
    visited[0][0] = True
    
    while que:
        n1, n2 = que.popleft()
        
        for i in range(4):
            x = n1 + dx[i]
            y = n2 + dy[i]
            
            if x >= 0 and y >= 0 and x < N and y < M:
                
                if data[x][y] != 0 and not visited[x][y]:
                    
                    data[x][y] = data[n1][n2] + 1
                    visited[x][y] = True
                    que.append((x, y))

BFS()
print(data[N- 1][M- 1])
# print(data)