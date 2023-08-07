import sys

N, K = map(int , sys.stdin.readline().split())

data = [i + 1 for i in range(N)]
output = []
i = 0
while data:
    i += K - 1
    if i < len(data):
        output.append(data.pop(i))
    else :
        i = i % len(data)
        output.append(data.pop(i))

print('<',end='')

for i in range(len(output)):
    if i != len(output) - 1:
        print(output[i],end=', ')
    else:    
        print(output[i],end='')
print('>')
