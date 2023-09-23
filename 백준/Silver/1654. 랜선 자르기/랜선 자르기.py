import sys

K, N = map(int, sys.stdin.readline().split())
data = [0] * K
for i in range(K) :
    data[i] = int(sys.stdin.readline())

data.sort()

left = 0
right = data[-1]
cnt = 0

def find(num):
    cnt = 0
    if num == 0 :
        num = 1
    for item in data:
        cnt += (item // num)
    return cnt

max_data = 0

# def round(num):
#     return int(num) + (1 if num - int(num) > 0.5 else 0) 

while left <= right:
    num = (left + right) // 2
    cnt = find(num)
    
    if cnt < N :
        right = num - 1
        # if num < min_data:
        #     min_data = num
    else :
        left = num + 1
        if num > max_data :
            max_data = num
        

answer = max_data

print(answer)    
    