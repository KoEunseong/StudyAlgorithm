import sys

N = int(input())

for _ in range(N):
    PS = sys.stdin.readline().strip()
    isTrue = True
    stack = []
    for i in range(len(PS)):
        if PS[i] == '(':
            stack.append(1)
        else :
            if len(stack) == 0:
                isTrue = False
                break
            stack.pop(0)
    
    if len(stack) == 0 and isTrue:
        print('YES')
    else:
        print('NO')
    