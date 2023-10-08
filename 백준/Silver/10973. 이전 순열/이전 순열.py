import sys

N = int(input())
data = list(map(int , sys.stdin.readline().split()))


n1 = 0
for i in range(1, len(data)):
    if data[i - 1] > data[i]:
        n1 = i

n2 = 0
for j in range(n1, len(data)):
    if data[j] < data[n1 - 1]:
        n2 = j
     
data[n1 - 1], data[n2] = data[n2], data[n1 - 1]

reversedata = list(reversed([item for item in data[n1:]]))

if n1 != 0:

    print(*(data[:n1] + reversedata))
else :
    print(-1)






# point = len(reversedata) - 1
# for i in range(len(reversedata) // 2):
#     reversedata[i], reversedata[point] = reversedata[point],reversedata[i]
#     point -= 1


