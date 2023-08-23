import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())

data = [[] for _ in range(N)]


for _ in range(M):
    n1, n2 = map(int ,sys.stdin.readline().split())
    data[n1].append(n2)
    data[n2].append(n1)


isTrue = False
visit_data = [False for _ in range(N)]

def DFS(n, depth):
    global isTrue        
    if depth == 5 :
        isTrue = True
        return
    visit_data[n] = True
    
    for item in data[n] :
        if not visit_data[item]:
            DFS(item, depth + 1)
    visit_data[n] = False
                        
for i in range(N):
    # visit_data = [False for _ in range(N)]
    DFS(i, 1)
    if isTrue:
        break

if isTrue :
    print(1)
else :
    print(0)