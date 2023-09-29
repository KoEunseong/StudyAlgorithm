import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
data = [[] for _ in range(N + 1)]
enterDegree = [0 for _ in range(N + 1)]

for i in range(1, M + 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    data[n1].append(n2)
    
for i in range(1, N + 1) :
    for item in data[i]:
        enterDegree[item] += 1
    
answer = []
myque = deque()

for i in range(1, N + 1):
    if enterDegree[i] == 0:
        myque.append(i)
        # enterDegree[i] -= 1
        # break

        
while myque:
    num = myque.popleft()
    answer.append(num)
    for i in data[num]:
        enterDegree[i] -= 1
        if enterDegree[i] == 0 :
            myque.append(i)
    
   
            
    
    
print(*answer)
        
        