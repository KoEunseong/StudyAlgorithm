import sys

N = int(input())
data = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0 for i in range(N)]

for i in range(N):
    
    
    # if data[stack[0]] < data[i]:
    #     stack.append(i)
    #     result[stack.pop(0)] = data[stack[-1]]
        
        
    #     # print(data[stack[i]])
    # else :
    #     stack.append(i)
        
    while stack and data[i] > data[stack[-1]]:
        result[stack.pop()] = data[i]
    stack.append(i)
    
while stack:
    result[stack.pop()] = -1
print(*result)
