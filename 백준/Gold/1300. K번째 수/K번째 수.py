import sys
sys.setrecursionlimit(10*6)

N = int(input())
k = int(input())

# mid = ((1 + N) // 2) ** 2
start = 1
end = k
answer = 0

while start <= end :
    count = 0
    mid = (start + end) // 2
    
    for i in range(1 , N + 1):
        num  = mid // i
        if num >= N:
            num = N
        count += num
    
    # if count == k :
    #     answer = mid
    #     break
    if count < k :
        start = mid +  1
    else :
        answer = mid
        end = mid - 1

print(answer)