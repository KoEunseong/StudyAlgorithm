import sys
start, end = map(int , sys.stdin.readline().split())

data = [True for i in range(end + 1)]
data[1] = False

for i in range(2, end + 1):
    if data[i] == True :
        for j in range(i + i, end + 1, i):
            data[j] = False

for i in range(start, end + 1):
    if data[i] :
        print(i)