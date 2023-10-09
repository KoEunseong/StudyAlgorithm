from queue import PriorityQueue
from collections import deque

def solution(priorities, location):
    myque = deque()
    for i in range(len(priorities)) :
        myque.append((priorities[i], i))
    
    cnt = 0
    while myque :
        max_num = max(myque)
        num = myque.popleft()
        
        if num[0] == max_num[0] :
            cnt += 1
            if location == num[1]:
                return cnt
        else :
            myque.append(num)
    
    


        
    
    answer = 0
    return answer