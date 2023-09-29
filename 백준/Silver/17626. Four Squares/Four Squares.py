import sys
import math

N = int(input())
i = 1
square_nums = []
answer = [0 for i in range(N + 1)]

while i <= math.sqrt(N):
    square_nums.append(i ** 2)
    i += 1
# print(square_nums)

def get_small(num):
    result = []
    for item in square_nums:
        if item > num :
            break
        result.append(item) 
    return result


for i in range(1, N + 1):
    arr = get_small(i)
    count = 4
    for item in arr:
        if answer[i - item] + 1 < count :
            count = answer[i - item] + 1
    answer[i] = count
print(answer[N])