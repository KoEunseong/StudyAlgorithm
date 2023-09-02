import sys

T = int(input())

dic = {}
for i in range(1, 14 + 1):
    dic[(0,i)] = i # 층 ,호

def getMember(f, n):
    if (f,n) in dic :
        return dic[(f, n)]
    sum = 0
    for i in range(1, n + 1):
        sum += getMember(f - 1, i)
    dic[(f, n)] = sum
    
    return dic[(f, n)]
        
for _ in range(T):
    floor = int(input())
    num = int(input())
    
    print(getMember(floor, num))
    
    
    
