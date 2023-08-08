import sys
    
N = int(input())
data = [0]
for _ in range(N):
    data.append(int(sys.stdin.readline()))


data = list(enumerate(data))
data2 = sorted(data,key = lambda x: x[1])

degree_data = [data2[i][0] - i for i in range(1, len(data))]

print(max(degree_data) + 1)