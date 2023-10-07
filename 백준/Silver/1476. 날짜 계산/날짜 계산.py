import sys

i1, i2, i3 = map(int , sys.stdin.readline().split()) # 16 29 20

n1, n2, n3 = 1, 1, 1

cnt = 0
while (n1, n2, n3) != (i1, i2, i3):
    cnt += 1
    n1 ,n2, n3 = n1 + 1, n2 + 1, n3 + 1
    if n1 > 15 :
        n1 = 1
    if n2 > 28 :
        n2 = 1
    if n3 > 19 :
        n3 = 1
    
print(cnt + 1)

    
