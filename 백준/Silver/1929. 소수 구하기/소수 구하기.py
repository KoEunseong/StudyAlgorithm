import sys
import math
M,N = map(int, sys.stdin.readline().split())

def isSosu(N):
    if N == 1:
        return False
    
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True
for i in range(M,N + 1):
    if isSosu(i):
        print(i)
