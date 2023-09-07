import sys

def gcd(n1, n2): #큰수 작은수
    while True:
        rest = n1 % n2
        
        if n1 % n2 == 0:
            return n2
        n1 = n2
        n2 = rest
N = int(input())        

for _ in range(N):
    n1, n2 = map(int, sys.stdin.readline().split())

    if n1 < n2 :
        n1 , n2 = n2, n1

    answer = 1

    while True:
        num = gcd(n1, n2)
        if num == 1:
            answer *= (n1 * n2)
            break
        answer *= num
        n1 //= num
        n2 //= num
        
    print(answer)    