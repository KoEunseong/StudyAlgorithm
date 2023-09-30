import sys
from collections import deque
N = int(input())

enterDegree = [0 for _ in range(N + 1)]
answer = [0 for _ in range(N + 1)]
data = [[] for i in range(N + 1)]
seconds = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    arr = list(map(int, sys.stdin.readline().split()))
    seconds[i] = arr[0]
    for j in range(1, len(arr) - 1):
        data[arr[j]].append(i)
        enterDegree[i] += 1

        
myque = deque()

for i in range(1, N + 1):
    if enterDegree[i] == 0:
        myque.append(i)

while myque:
    num = myque.popleft() # 1
    
    for item in data[num]: # 2 3 4
        enterDegree[item] -= 1
        answer[item] = max(answer[item], answer[num] + seconds[num]) 
        
        if enterDegree[item] == 0:
            myque.append(item)
            
for i in range(1, N + 1):
    print(answer[i] + seconds[i])