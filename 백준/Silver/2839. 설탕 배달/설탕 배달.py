import sys

N = int(sys.stdin.readline())

if N <= 5:
    if N == 3 or N == 5:
        print(1)
    else :
        print(-1)
else :
    data = [-1 for _ in range(N + 1)]



    data[3] = 1
    data[5] = 1

    for i in range(6, N + 1):
        if data[i - 3] == -1 and data[i - 5] == -1:
            continue
        elif data[i - 3] == -1:
            data[i] = data[i - 5] + 1
        elif data[i - 5] == -1:
            data[i] = data[i - 3] + 1
        else :
            data[i] = min(data[i - 3], data[i -5]) + 1
    print(data[-1])
        
        
