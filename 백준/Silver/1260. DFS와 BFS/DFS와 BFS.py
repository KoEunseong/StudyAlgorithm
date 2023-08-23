import sys
from collections import deque
sys.setrecursionlimit(10**7)

V, E, start = map(int, sys.stdin.readline().split())

data = [[] for _ in range(V + 1)]



for _ in range(E):
    n1, n2 = map(int , sys.stdin.readline().split())
    data[n1].append(n2)
    data[n2].append(n1)

for item in data :
    item.sort()

def DFS(start):
    print(start, end = ' ')
    visit_data[start] = True
    
    for item in data[start] :
        if not visit_data[item] :
            DFS(item)  

def BFS(start):
    que = deque()
    que.append(start)
    visit_data[start] = True
    
    while que:
        a = que.pop()
        print(a,end=' ')
        for item in data[a]:
            if not visit_data[item] :
                que.appendleft(item)
                visit_data[item] = True
        

visit_data = [False for _ in range(V + 1)]
DFS(start)
print()
visit_data = [False for _ in range(V + 1)]
BFS(start)