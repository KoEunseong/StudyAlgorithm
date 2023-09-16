import sys
from collections import deque
A, B, C = map(int, sys.stdin.readline().split())

data = (0, 0, C)
visited = [data]
# dic = {C : C}
answer = [C]

def BFS(data):
    myque = deque()
    myque.append(data)
    
    while myque :
        present = myque.popleft()
        for i in range(3): #i 가 start고 n1,n2가 target
            n1 , n2 = (i + 1) %3 , (i + 2) %3 
            if present[i] == 0:
                continue
            result = Pour(present, i, n1)
            result2 = Pour(present, i, n2)
            
            if result not in visited :
                visited.append(result)
                myque.append(result)
                if result[0] == 0 and result[2] not in answer:
                    answer.append(result[2])
            
            if result2 not in visited :
                visited.append(result2)
                myque.append(result2)
                
                if result2[0] == 0 and result2[2] not in answer:
                    answer.append(result2[2])
                
    
def Pour(water, start, target):
    # result = [water[0], water[1], water[2]]
    result = list(water)
    
    if target == 0 :
        limit = A
    elif target == 1 :
        limit = B
    else :
        limit = C
    rest = 0
    
    if water[start] > limit - water[target] : 
        rest = water[start] - (limit - water[target])
        inputWater = limit
    
    else :
        inputWater = water[start] + water[target]
    
    result[start] = rest
    result[target] = inputWater
    
    return (result[0],result[1],result[2])

BFS(data)
# print(visited)    
answer.sort()
print(*answer)


