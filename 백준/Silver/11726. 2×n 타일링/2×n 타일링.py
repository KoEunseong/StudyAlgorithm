import sys

N = int(input())
answer = [0 for i in range(1000 + 1)]
# answer[1] = 0
answer[1] = 1
answer[2] = 2   


for i in range(3, 1000 + 1): 
    answer[i] = answer[i - 1] + answer[i - 2]
print(answer[N] % 10007)

        
        
