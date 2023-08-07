import sys
from collections import deque
N = int(input())

command = []
mydeq = deque()
for _ in range(N):
    command.append(sys.stdin.readline().strip().split())

for item in command:
    if item[0] == 'push_back':
        mydeq.append(item[1])
        
    elif item[0] == 'push_front':
        mydeq.appendleft(item[1])
        
    elif item[0] == 'pop_back':
        if len(mydeq) == 0:
            print(-1)
        else : 
            print(mydeq.pop())
            
    elif item[0] == 'pop_front':
        if len(mydeq) == 0:
            print(-1)
        else : 
            print(mydeq.popleft())
            
    elif item[0] == 'size':
        print(len(mydeq))
    elif item[0] == 'empty':
        if len(mydeq) == 0:
            print(1)
        else :
            print(0)
    elif item[0] == 'back':
        if len(mydeq) == 0:
            print(-1)
        else :
            print(mydeq[-1])
    elif item[0] == 'front':
        if len(mydeq) == 0:
            print(-1)
        else :
            print(mydeq[0])
    