import sys

N = int(input())
stack = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0 :
        stack.pop()
    else :
        stack.append(num)
print(sum(stack))