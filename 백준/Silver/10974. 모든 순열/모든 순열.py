import sys

N = int(input())
data = [i for i in range(1, N + 1)]


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
  

# print(getNextPermutation([2, 3, 1]))
permutation = data
temp = 0
while True:
    print(*permutation)
    per = getNextPermutation(permutation)
    if per == -1:
        break
    permutation = per
    temp += 1