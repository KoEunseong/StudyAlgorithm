import sys
from queue import PriorityQueue

N = int(input())
data = [-int(sys.stdin.readline()) for i in range(N)]
myque = PriorityQueue()
for item in data:
    if item == 0:
        if myque.empty():
            print(0)
        else :
            print(-myque.get())
    
    else :
        myque.put(item)
