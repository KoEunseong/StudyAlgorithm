import sys

N, M = map(int , sys.stdin.readline().split())

data = []
for i in range(N):
    line = sys.stdin.readline().strip()
    data.append(list(line))
a = ['W', 'B'] * 4
b = ['B', 'W'] * 4


def get_cnt(x, y):
    cnt1 = 0 #whiteFirst
    cnt2 = 0 #blackFirst
    
    for i in range(x, x + 8):
        m = 0
        for j in range(y, y + 8):        
            if i % 2 == 0 :
                if data[i][j] != a[m]:
                    cnt1 += 1
                if data[i][j] != b[m]:
                    cnt2 += 1
            else :
                if data[i][j] != b[m]:
                    cnt1 += 1
                if data[i][j] != a[m]:
                    cnt2 += 1
            m += 1
    return min(cnt1, cnt2)

# answer = get_cnt(0,0)
answer = 32
for i in range(N - 7):
    for j in range(M - 7):
        temp = get_cnt(i,j)
        if answer > temp:
            answer = temp
print(answer)