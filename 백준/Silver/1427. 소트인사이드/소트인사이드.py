import sys

num = int(input())
data = []


i = 10
while num :
    data.insert(0,num % i)
    num //= i

for i in range(len(data)):
    maxi = (data[i], i)
    for j in range(i + 1,len(data)):
        if data[j] > maxi[0]:
            maxi = (data[j], j)
    
    temp = data[i]
    data[i] = maxi[0]
    data[maxi[1]] = temp
    

# data.sort(reverse=True)

for i in data:
    print(i,end='')



