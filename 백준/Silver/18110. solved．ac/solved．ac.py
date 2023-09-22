import sys
from queue import PriorityQueue

N = int(input())

def round(N):
    num = N - int(N)
    if num >= 0.5 :
        return int(N) + 1
    else :
        return int(N)

cut = int(round(N * 0.15))    
data = [0 for _ in range(N)]

min_arr = PriorityQueue()
max_arr = PriorityQueue()

for i in range(N):
    num = int(sys.stdin.readline())
    data[i] = num
    min_arr.put(num)
    max_arr.put(-num)    
    

removing = 0
for i in range(cut):
    
    removing += min_arr.get()
    removing += -(max_arr.get())

answer = 0

if N != 0:
    answer = (sum(data) - removing) / (N - (cut * 2))
print(round(answer))



