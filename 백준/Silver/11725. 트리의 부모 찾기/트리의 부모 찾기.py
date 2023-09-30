import sys
sys.setrecursionlimit(10**7)
N = int(input())
data = [[] for i in range(N + 1)]
answer = [0 for i in range(N + 1)]
for i in range(N - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    data[n1].append(n2)
    data[n2].append(n1)
    
visited = [False for i in range(N + 1)]

def DFS(start):
    num = data[start]
    visited[start] = True
    
    for item in num :
        if not visited[item]:
            answer[item] = start
            DFS(item)
            
DFS(1)
for i in range(2, N + 1):
    
    print(answer[i])
