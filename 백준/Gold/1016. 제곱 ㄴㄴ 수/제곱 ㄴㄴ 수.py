import sys
import math

min, max = map(int ,sys.stdin.readline().split())

data = [1] * (max - min + 1)

for i in range(2, (int(math.sqrt(max)) + 1)):
    
    num = i ** 2
    if min % num == 0: 
        start = 0
    else :
        start = (num - (min % num))  # 4 -
    
    
    for j in range(start, len(data), num):    
        data[j] = 0

# print(data)
count = 0
for item in data :
    if item == 1 :
        count += 1
print(count)

    


