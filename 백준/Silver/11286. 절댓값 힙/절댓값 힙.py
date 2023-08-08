import sys
from collections import deque
from queue import PriorityQueue

N =int(input())
# stack = []
myque = PriorityQueue()
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))



for num in numbers:
    
    
    if num == 0:
        if myque.empty():
            print(0)
        else :
            print(myque.get()[1])
            
    else :    
        myque.put((abs(num), num))
