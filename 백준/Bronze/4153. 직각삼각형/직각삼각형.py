import sys

answer = []
while True:
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()
    
    if data[-1] == 0:
        break
    elif data[0]**2 + data[1]**2 == data[2]**2:
        # print('right')
        answer.append(1)
    else :
        # print('wrong')  
        answer.append(0)

for item in answer:
    if item:
        print('right')
    else : 
        print('wrong')
    
    