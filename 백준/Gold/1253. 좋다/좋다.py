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

print(count)
    