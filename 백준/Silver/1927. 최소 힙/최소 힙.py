import sys
from queue import PriorityQueue

N = int(input())
myque = PriorityQueue()

data = [int(sys.stdin.readline()) for i in range(N)]

for item in data:
    if item == 0:
        if myque.empty():
            print(0)
        else :
            print(myque.get())
    else :
        myque.put(item)