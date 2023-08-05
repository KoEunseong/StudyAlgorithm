import sys

N = int(input())

data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))

myst = []
i = 1
answer = []
impossible = False
for index in range(N):
        
    while True:
        if i > N and myst[0] != data[index]:
            impossible = True
            break
        
        if len(myst) != 0 and myst[0] == data[index]:
            answer.append('-')
            myst.pop(0)
            break
        
        answer.append('+')
        myst.insert(0, i)
        i += 1
    if impossible :
        break

if len(myst) == 0 :
    for item in answer:
        print(item)
else : 
    print('NO')       
        
    