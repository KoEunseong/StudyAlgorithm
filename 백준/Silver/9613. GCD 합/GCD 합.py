import sys
import math

t = int(input())

for _ in range(t):
    data = list(map(int, sys.stdin.readline().split()))
    N = data[0]
    sum = 0
    for i in range(1, N ):
        for j in range(i + 1, N + 1):
            # print(data[i], data[j] )
            sum += math.gcd(data[i], data[j])
    print(sum)