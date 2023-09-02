import sys

N = int(input())
string = sys.stdin.readline().strip()
M = 1234567891
r = 31

dic = {}

a = 97
for i in range(1, 26 + 1):
    dic[chr(a)] = i
    a += 1


sum = 0
for i in range(N):
    sum += dic[string[i]] * (r ** i)

print(sum % M)