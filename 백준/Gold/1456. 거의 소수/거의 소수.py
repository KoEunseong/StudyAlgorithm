import sys
import math
A,B = map(int , sys.stdin.readline().split()) 

sosuData = [1] * (int(math.sqrt(B)) + 1)
sosuData[0] = 0
sosuData[1] = 0
for i in range(2, int(math.sqrt(B)) + 1):
    if sosuData[i] == 0:
        continue
    for j in range(i * i, int(math.sqrt(B)) + 1, i):
        sosuData[j] = 0

count = 0
for i in range(2, len(sosuData)):
    
    if sosuData[i] == True :
        temp = i
        j = 2
        while True :
            num = temp ** j
            if num / A < 1 :
                j += 1
                continue
            if num / B > 1 :
                break
            count += 1
            j += 1
            
print(count)
