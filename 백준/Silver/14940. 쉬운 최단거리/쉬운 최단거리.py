import sys
from collections import deque

row, column = map(int , sys.stdin.readline().split())

moveX = [-1, 1, 0 , 0] #좌우상하
moveY = [0, 0 , 1, -1]

answer = [[0 for _ in range(column)] for _ in range(row)]
visited = [[False for _ in range(column)] for _ in range(row)]

data = []
def find(arr, num):
    for i in range(len(arr)) :
        if arr[i] == num:
            return i
            
    
for i in range(row):
    arr = list(map(int, sys.stdin.readline().split()))
    if 2 in arr :
        target = (i, find(arr, 2))
    data.append(arr)
    
def BFS(target):
    n1, n2 = target
    visited[n1][n2] = True
    
    myque = deque()
    myque.append(target)
    
    while myque: 
        point = myque.popleft()
        for i in range(4):
            x = point[0] + moveX[i]
            y = point[1] + moveY[i]
            
            if (x >= 0 and y >= 0 and x < row and y < column) and not visited[x][y] : 
                visited[x][y] = True
                if data[x][y] == 0:
                    continue
            
                else : 
                    visited[x][y] = True
                    answer[x][y] = answer[point[0]][point[1]] + 1
                    myque.append((x, y))
                
BFS(target)
for i in range(row):
    for j in range(column):
        num = answer[i][j]
        if num == 0 and visited[i][j] == False and data[i][j] != 0:
            
            print(-1, end=' ')
        else : 
            print(answer[i][j], end=' ')
    print()
# print(answer)
    
    
