import sys
from collections import deque
N,L = map(int , sys.stdin.readline().split())

data = list(map(int , sys.stdin.readline().split()))
mydeque = deque()

for i in range(N):
    t = (i + 1, data[i])
    # for j in range(len(mydeque) - 1, 0 - 1, -1):
    while mydeque :
        if mydeque[-1][1] > t[1]:
            mydeque.pop()
        else:
            break
            # pass
    mydeque.append(t)
    if mydeque[-1][0] - mydeque[0][0] >= L:
        mydeque.popleft()
    print(mydeque[0][1],end= ' ')