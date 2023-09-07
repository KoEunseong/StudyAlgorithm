import math

N = int(input())

# data = [i for i in range(0, N + 1)] 

result = N

for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
        result -= (result // i)
        
        while N % i == 0:
            N = N // i
        
        


if N > 1:
    result -= result // N
print(result)

    
    
    
    # if data[i] != i :
    #     continue
    # for j in range(i, N + 1, i):
        
    #     data[j] = data[j] - (data[j] // i)

# print(data[-1])
