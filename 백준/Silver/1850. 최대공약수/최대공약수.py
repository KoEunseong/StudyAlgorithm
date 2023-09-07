import sys

A,B = map(int , input().split())

if A < B :
    A, B = B, A

def gcd(n1, n2): # big small
    while n2 != 0:
        num = n1 % n2
        n1 = n2
        n2 = num
    return n1

count = gcd(A, B)
for i in range(count):
    print(1,end='')