import sys
def com(N):
    output = (N * (N - 1)) // 2
    return output


N , M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
sum_data = []
sum = 0
for i in data:
    sum += i
    sum_data.append(sum)

answer = 0
for i in range(N):
    sum_data[i] = sum_data[i] % M
    if sum_data[i] == 0 :
        answer += 1


dic = {}
for i in range(N):
    if sum_data[i] in dic :
        dic[sum_data[i]] += 1
    else :
        dic[sum_data[i]] = 1


for i in dic:
    answer += com(dic[i])
print(answer)

