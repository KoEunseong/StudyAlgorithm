import sys

def factorial(N):
    output = 1
    for i in range(1, N + 1):
        output *= i
    return output

N = int(sys.stdin.readline())

N = str(factorial(N))

zero_count = 0
for i in range(-1 , -len(N), -1):
    if N[i] != '0':
        break
    zero_count += 1
    

print(zero_count)