import sys
from queue import PriorityQueue
import heapq

N = int(input())

minus_data = []
plus_data = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num > 0 :
        heapq.heappush(plus_data, -num)
    else :
        heapq.heappush(minus_data, num)

sum = 0

while len(minus_data) > 0: #minus part
    if len(minus_data) == 1:
        sum += heapq.heappop(minus_data) 
    else :
        n1 = heapq.heappop(minus_data)
        n2 = heapq.heappop(minus_data)
        sum += ( n1 * n2 )

while len(plus_data) > 0:
    if len(plus_data) == 1:
        sum += -(heapq.heappop(plus_data))
    else :
        n1 = -heapq.heappop(plus_data) 
        n2 = -heapq.heappop(plus_data)
        if n1 * n2 > n1 + n2 :
            sum += (n1 * n2)
        else :
            sum += n1 + n2

print(sum)