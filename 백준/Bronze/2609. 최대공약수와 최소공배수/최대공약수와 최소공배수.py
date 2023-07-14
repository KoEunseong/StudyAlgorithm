import sys

n1, n2 = map(int,sys.stdin.readline().split())

lcm = max(n1,n2) #최소공배수

t1, t2 = n1, n2
while t2 != 0:
    temp = t1 % t2
    t1 = t2
    t2 = temp
    
print(t1)

i = 1
while n1 * n2 > lcm:
    lcm = n1 * i
    if lcm % n2 == 0:
        break
    i += 1
print(lcm)
    
