import sys
sys.setrecursionlimit(10**7) # 10에 7승 만큼 최대 재귀한도 깊이 변경 
N, M = map(int ,sys.stdin.readline().split())
visit_list = [False for _ in range(N + 1)]
answer = 0

data = [[] for _ in range(N + 1)]    


for i in range(M):
    n1, n2 = map(int , sys.stdin.readline().split())
    data[n1].append(n2)
    data[n2].append(n1)


def DFS(v):
    visit_list[v] = True
    for item in data[v] :
        if not visit_list[item]:
            DFS(item)
            
for i in range(1, N + 1):
    if not visit_list[i] :
        answer += 1
        DFS(i)

print(answer)