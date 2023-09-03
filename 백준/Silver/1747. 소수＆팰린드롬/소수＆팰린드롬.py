from math import sqrt
N = int(input())

sosuData = [1] * (1000000 + 2) * 2
sosuData[1] = 0
for i in range(2, int(sqrt(len(sosuData))) + 1):
    if sosuData[i] == 0:
        continue
    for j in range(i * i, (1000001 + 1) * 2, i):
        
        sosuData[j]  = 0

def ispalindrome(num):
    num = str(num)
    j = -1
    for i in range(len(num) // 2):
        if num[i] != num[j]:
            return 0
        j -= 1
    return num

for i in range(N, (1000000 + 2) * 2):
    
    if sosuData[i] == 1:
        if ispalindrome(i) != 0:
            print(i)
            break