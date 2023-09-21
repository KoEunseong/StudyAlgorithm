import sys
N = int(input())
M = int(input())

road = []
data = [i for i in range(N + 1)]

for _ in range(N):
    road.append(list(map(int, sys.stdin.readline().split())))

wanted = list(map(int,sys.stdin.readline().split()))

def union(n1, n2):
    a = find(n1)
    b = find(n2)
    
    if a != b :
        data[b] = a

def find(num):
    if data[num] == num :
        return num
    else :
        data[num] = find(data[num])
        return data[num]
    

for i in range(N):
    for j in range(N):
        if road[i][j] == 1:
            union(i + 1, j + 1)

# print(data)

a = find(wanted[0])
isAnswer = 'YES'
for item in wanted :
    num = find(item)
    if num != a :
        isAnswer = 'NO'
        
print(isAnswer)