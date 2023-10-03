import sys
from collections import deque

N, K = map(int , sys.stdin.readline().split())

arr = [100000 for i in range(1000000 + 1)]
temp = 1
visited = [False for i in range(1000000 + 1)]


def BFS(num):
    myque = deque()  
    temp = 0
    
    
    myque.append(num)
    visited[num] = True
    arr[num] = temp
    
    
    while myque:
        num = myque.popleft()
        
        data = [num * 2, num -1 , num + 1]
        
        if arr[num] > arr[K]:
            continue
        
        for item in data : # 10 4 6
            if item < 0 :
                continue
            
            if not visited[item]:
                arr[item] = min(arr[item], arr[num] + 1)
                visited[item] = True

                if item >= K:
                    arr[K] = min(arr[K], item - K + arr[item])
                else :
                    myque.append(item)
            

if N >= K:
    print(N - K)
else :
    BFS(N)   
    print(arr[K])
