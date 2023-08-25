import sys
sys.setrecursionlimit(10*6)
from collections import deque

testCase = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


for _ in range(testCase) :
    row, column , cabbage = map(int, sys.stdin.readline().split())
    data = [[0 for _ in range(column)] for _ in range(row)]
    
    for _ in range(cabbage):
        x, y = map(int ,sys.stdin.readline().split())
        data[x][y] = 1

    visited = [[False for _ in range(column)] for _ in range(row)]

    bug = 0

    def BFS(n1, n2):
        global bug
        bug += 1
        que = deque()
        visited[n1][n2] = True
        que.append((n1, n2))
        
        while que:
            now  = que.popleft()
            
            for i in range(4):
                x = now[0] + dx[i]
                y = now[1] + dy[i]
                
                if x >=0 and y >= 0 and x < row and y < column :
                    if data[x][y] != 0 and not visited[x][y] :
                        visited[x][y] = True
                        que.append((x, y))
                        


    for i in range(row):
        for j in range(column):
            if not visited[i][j] and data[i][j] != 0:
                BFS(i, j)
    print(bug)