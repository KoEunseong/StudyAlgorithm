import sys
sys.setrecursionlimit(10**6)

N = int(input())
M = int(input())

data = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = map(int ,sys.stdin.readline().split())
    data[n1].append(n2)
    data[n2].append(n1)
    
# print(data)
visited = [False for _ in range(N + 1)]

def DFS(v):
    visited[v] = True
    
    for i in data[v]:
        if not visited[i] :
            DFS(i)
    

answer = 0
DFS(1)

for item in visited :
    if item :
        answer += 1
        
print(answer -1)