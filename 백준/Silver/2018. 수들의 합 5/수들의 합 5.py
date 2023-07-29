import sys

N = int(input())

# data = [i for i in range(N + 1)]
start = 1
end = 1

count = 1
if N == 1 :
    count -= 1
sum = 0



for i in range(N):
    # sum += data[end]
    sum += end
    if sum < N :
        end += 1
    elif sum == N:
        count += 1
        # sum -= data[start]
        sum -= start
        start += 1
        end += 1
    else:
        # sum -= (data[start] + data[end])
        sum -= (start + end)
        start += 1
        
        
    
     

print(count)