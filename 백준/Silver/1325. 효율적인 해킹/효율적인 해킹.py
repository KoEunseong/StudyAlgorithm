import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
data = [[] for i in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int , sys.stdin.readline().split())
    data[n2].append(n1)
    
# print(data)
# 아 이제 깨달았다1!!!!!!

visited = [False for _ in range(N)]

def BFS(X):
    visited = [False for _ in range(N + 1)]
    answer = 0
    myque = deque()
    visited[X] = True
    myque.append(X)
    
    while myque :
        num = myque.popleft()
        for item in data[num]:
            if not visited[item]:
                visited[item] = True
                answer += 1
                myque.append(item)

    return answer

answer = 0
answer_list = []
for i in range(1, N + 1):
    # visited = [False for _ in range(N + 1)]
    count = BFS(i)
    # print(count)
    if count > answer:
        answer = count
        answer_list = [i]
    elif count == answer :
        answer_list.append(i)
print(*answer_list)


# visited = [False for _ in range(N + 1)]
# BFS(answer[1])
# print(answer)
# print(visited)

# print(visited)
# for item in visited:
#     if item :
#         print(item)
    
                    
    