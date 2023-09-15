import sys
sys.setrecursionlimit(10**6)

K = int(input())

def DFS(x):
    global isAnswer
    visited[x] = True

    for item in data[x]:
        if visited[item] == False:
            check[item] = (check[x] + 1) % 2
            DFS(item)
        
        elif check[item] == check[x]:
            isAnswer = False
#             return
        

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    data = [[] for i in range(V + 1)]
    
    for _ in range(E):
        n1, n2 = map(int, sys.stdin.readline().split())
        data[n1].append(n2)
        data[n2].append(n1)
    
    isAnswer = True
    visited = [False for _ in range(V + 1)]
    check = [0 for _ in range(V + 1)]
    
    for i in range(1, V + 1):
        # if visited[i] == - 1 :
        #     DFS(i, 0)
        if isAnswer :
            DFS(i)
        else :
            break

    if isAnswer :
        print('YES')
    else :
        print('NO')
    
        