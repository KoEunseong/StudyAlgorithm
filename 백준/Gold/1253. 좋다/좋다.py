import sys

N = int(input())

data = list(map(int, sys.stdin.readline().split()))

data.sort()

count = 0




index = 0

for item in data:
    
    start = 0
    end = N - 1
    
    while start < end:
        if start == index:
            start += 1
            continue
        if end == index:
            end -= 1
            continue
        
        sum = data[start] + data[end]
        if sum < item:
            start += 1
        elif sum > item:
            end -= 1
        else :
            count += 1
            break
            
    index += 1
    
    
            
    
    
    
    
    # sum = data[start] + data[end]
    # if sum < item:
    #     if start != end - 1:
    #         start += 1
    #     else:
    #         end += 1
    #         ip += 1
    #         continue
    # elif sum > item:
    #     if start != end - 1:
    #         end -= 1
    #     else:
            
    #         continue
    # else :
    #     count += 1
    #     end += 1
print(count)
    