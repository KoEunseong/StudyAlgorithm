N = int(input())
list_a = []

sum = 0
for i in range(1,10000):
    sum += i
    list_a.append(sum)
# print(list_a[-1])

count = 0
for i in range(len(list_a)):
    if N <= list_a[i]:
        count = i
        break
start = list_a[count -1] + 1
end = list_a[count]


answer = [(count + 1 - i, i + 1) for i in range(end - start + 1)]
if count % 2 != 0:
    answer.reverse()
if N == 1:
    print('1/1')
else:
    print("{}/{}".format(*answer[N - start]))

