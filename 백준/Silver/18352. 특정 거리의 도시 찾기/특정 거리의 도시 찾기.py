import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M, K, X = map(int, sys.stdin.readline().split()) # 노드의 갯수, 엣지 수 ,원하는 최단거리, 출발시점
data = [[] for i in range(N + 1)]

for _ in range(M):
    n1 , n2 = map(int, sys.stdin.readline().split())
    data[n1].append(n2)
    
visited = [False for _ in range(N + 1)]

answer = 0
depth_data = [300000 for i in range(N + 1)]

def BFS(x):
    myque = deque()
    visited[x] = True
    myque.append(x)
    # depth = 0
    depth_data[x] = 0
    
    while myque:
        num = myque.popleft()
        depth = depth_data[num]
        for item in data[num]:
            # if not visited[item] :
            if depth_data[item] > depth :
                visited[item] = True
                myque.append(item)
                depth_data[item] = depth + 1
                
BFS(X)
# print(depth_data)

# def DFS(x, depth) : #출발점, 거리
#     # visited[x] = True
#     if depth_data[x] < 0 or depth_data[x] > depth :
#         depth_data[x] = depth
    
#     for item in data[x]:
#         # if not visited[item] :
#         DFS(item, depth + 1)

# DFS(X, 0) 최단거리의 경우 BFS가 맞는 거 같음

if K in depth_data:
    for i in range(1, N + 1):
        if depth_data[i] == K:
            print(i)
else :
    print(-1)
    