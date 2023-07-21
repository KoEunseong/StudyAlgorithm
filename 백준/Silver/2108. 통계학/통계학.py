import sys
        
N = int(input())
data = {}
data2 = []
sum = 0
for i in range(N):
    num = int(sys.stdin.readline())
    sum += num
    data2.append(num)
    if num in data:
        data[num] += 1
    else :
        data[num] = 1
data2.sort()
mode_data = sorted(data.items(), key = lambda x : (-x[1], x[0])) 

# print('------------')
print(round(sum / N))
print(data2[N // 2])
# print(mode_data)
if len(mode_data) > 1 and mode_data[0][1] == mode_data[1][1]:
    print(mode_data[1][0])
else :
    print(mode_data[0][0])
print(max(data) - min(data))