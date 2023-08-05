import sys
from collections import deque

N = int(input())

class myqueue :
    def __init__(self) :
        self.mydeq = deque()
        
    def pop(self):
        if len(self.mydeq) == 0:
            return -1
        return self.mydeq.pop()
    
    def empty(self):
        if len(self.mydeq) == 0:
            return 1
        else :
            return 0
    def front(self):
        if len(self.mydeq) == 0:
            return -1
        return self.mydeq[-1]
    def back(self):
        if len(self.mydeq) == 0:
            return -1
        return self.mydeq[0]
myq = myqueue()

for _ in range(N):
    item = sys.stdin.readline().split()
    if item[0] == 'push':
        myq.mydeq.appendleft(item[1])
    elif item[0] == 'pop':
        print(myq.pop())
    elif item[0] == 'size':
        print(len(myq.mydeq))
    elif item[0] == 'empty':
        print(myq.empty())
    elif item[0] == 'front':
        print(myq.front())
    elif item[0] == 'back':
        print(myq.back())