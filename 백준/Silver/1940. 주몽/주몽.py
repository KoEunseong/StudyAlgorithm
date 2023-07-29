import sys

N = int(input())
M = int(input())

data = list(map(int, sys.stdin.readline().split()))

data.sort()

start = 0 
end = len(data) - 1
sum = 0 
count = 0

while start < end:
    sum = (data[start] + data[end])
    if sum < M:
        start += 1
    elif sum > M:
        end -= 1
    else : # sum == M
        count += 1
        start += 1
print(count)