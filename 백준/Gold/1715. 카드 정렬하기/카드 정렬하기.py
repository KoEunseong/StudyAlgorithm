import sys
from queue import PriorityQueue
N = int(input())

myque = PriorityQueue()

for i in range(N):
    num = int(sys.stdin.readline())
    myque.put(num)
    
sum = 0

while myque.qsize() > 1 :
    n1 = myque.get()
    n2 = myque.get()
    num = n1 + n2
    sum += num
    myque.put(num)

print(sum)
