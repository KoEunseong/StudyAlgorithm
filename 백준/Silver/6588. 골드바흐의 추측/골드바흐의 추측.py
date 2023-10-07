import sys
import math

data = [True for i in range(1000000 + 1)]

data[1] = False

sosu = []
for i in range(2, 1000000 + 1):
    if not data[i] :
        continue
    
    for j in range(i + i, 1000000 + 1 , i):
        data[j] = False

while True :
    num = int(sys.stdin.readline())
    n1, n2 = 0, 0
    if num == 0 : 
        break
    
    # for item in sosu :
    #     if num - item in sosu:
    #         n1, n2 = item, num - item
    #         break
    for i in range(len(data)):
        if data[i] and i % 2 != 0:
            if data[num - i] :
                n1, n2 = i, num - i
                break
    
    print('{} = {} + {}'.format(num, n1, n2))
    