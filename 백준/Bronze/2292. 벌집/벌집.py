import sys
sys.setrecursionlimit(10**6)

N = int(input())

i = 1
count = 0

while True:
    count += 1
    if N <= i:
        break
    
    i += (6 * count)
    

print(count)    
