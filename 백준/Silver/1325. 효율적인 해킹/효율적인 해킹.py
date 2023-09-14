import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
data = [[] for i in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int , sys.stdin.readline().split())
    data[n1].append(n2)
    
visited = [0 for _ in range(N + 1)]    

def BFS(X):
    
    myque = deque()
    myque.append(X)
    visit[X] = True
    while myque :
        num = myque.popleft()
        
        for item in data[num]:
            if not visit[item] :
                visit[item] = True
                visited[item] = visited[item] + 1
                myque.append(item)

for i in range(1, N + 1):
    visit = [False for _ in range(N + 1)]    
    BFS(i)

max_data = max(visited)
for i in range(1, N + 1):
    if visited[i] == max_data :
        print(i, end=' ')
