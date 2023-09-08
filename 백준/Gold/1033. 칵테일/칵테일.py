import sys
import math

N = int(input())
data = [[] for i in range(N)] 

def gcd(n1, n2):
    
    if n1 < n2 :
        n1 , n2 = n2 , n1
    
    while n2 != 0:
        num = n1 % n2
        n1 = n2
        n2 = num
    return n1

lcm = 1
for i in range(N - 1):
    p1, p2, n1, n2 = map(int , sys.stdin.readline().split())
    lcm *= (n1 * n2)
    lcm //= gcd(n1, n2)
    
    data[p2].append((p1, n2, n1))
    data[p1].append((p2, n1, n2))


visited = [False for i in range(N)]
answer = [0] * N

answer[0] = lcm

def DFS(i):
    visited[i] = True
    for item in data[i]:
        if visited[item[0]] == False :
            answer[item[0]] = item[2] * answer[i] // item[1]
            DFS(item[0])

DFS(0)
num = answer[0]
for i in range(len(answer) - 1):
    num = gcd(num, answer[i + 1])

for item in answer :
    print(item // num, end=' ')
