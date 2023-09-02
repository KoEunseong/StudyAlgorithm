import sys

N = int(input())


answer = 0
for i in range(1, N + 1):
    sum = i
    str_num = str(i)
    for j in range(len(str_num)):
        sum += int(str_num[j])
    if N == sum:
        answer = i
        break
print(answer)
