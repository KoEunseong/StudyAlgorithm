import sys

N = int(input())
data = list(map(int , sys.stdin.readline().split()))
data.sort()

sum = 0
answer = 0
for item in data:
    sum += item
    answer += sum
    
print(answer)
