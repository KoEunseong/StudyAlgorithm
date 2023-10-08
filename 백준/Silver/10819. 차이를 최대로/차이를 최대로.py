import sys
import math
N = int(input())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

def calculate(arr):
    result = 0
    for i in range(1, len(arr)):
        result += abs(arr[i - 1] - arr[i])
    return result

def getNextPermutation(permutation):
    result = permutation
    n1 = 0
    for i in range(1, N):
        if permutation[i - 1] < permutation[i] :
            n1 = i

    n2 = 0
    for j in range(n1, N):
        if permutation[n1 - 1] < permutation[j]:
            n2 = j
    
    result[n1 - 1], result[n2] = result[n2], result[n1 - 1]
    
    
    
    if n1 == 0 :
        result = -1
    else :
        result = result[: n1] + list(reversed(result[n1: ]))    
    
    return result

arr = data

answer = 0

while arr != -1:
    
    answer = max(answer, calculate(arr))
    arr = getNextPermutation(arr)
    
print(answer)