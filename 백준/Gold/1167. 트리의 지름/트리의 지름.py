import sys
sys.setrecursionlimit(10**6)
from collections import deque

N = int(input())
data = [[] for _ in range(N + 1)]
distance = [0 for _ in range(N + 1)]
for i in range(N):
    
    line = list(map(int, sys.stdin.readline().split()))
    
    for i in range(1,len(line),2):
        if line[i] != -1:
            n1, n2 = line[i], line[i + 1]
            data[line[0]].append((n1, n2))
        else :
            break

visited = [False for _ in range(N + 1)]

def BFS(start):
    que = deque()
    que.append(start)
    
    visited[start] = True
    while que :
        a = que.popleft() # 4
            
        
        for item in data[a]:
            if not visited[item[0]] :
                
                que.append(item[0]) # 4
                visited[item[0]] = True
                distance[item[0]] = distance[a] + item[1]
    
BFS(1)

max_data = distance[1]
index = 1
for i in range(1, len(distance)): # 
    if distance[i] > max_data : 
        max_data = distance[i]
        index = i

visited = [False for _ in range(N + 1)]
distance = [0 for _ in range(N + 1)]    

BFS(index)
print(max(distance))
# for i in range(N):
    # visited = [False for _ in range(N + 1)]
    # distance = [0 for _ in range(N + 1)]    
#     BFS(i)
#     answer.append(max(distance))
    
    
# visited = [False for _ in range(N + 1)]
# distance = [0 for _ in range(N + 1)]
