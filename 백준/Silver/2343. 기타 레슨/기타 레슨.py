import sys


N, M = map(int , sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

start = max(data)

end = sum(data)

while start <= end :
    
    mid = (start + end) // 2
    numOfbluray = 1
    hap = 0
    
    for item in data :
        hap += item
        if hap > mid :
            numOfbluray += 1
            hap = item
        
        if numOfbluray > M :
            break
        
    if numOfbluray > M : #impossible
        start = mid + 1
    else :
        end = mid - 1

print(start)
