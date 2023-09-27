import sys

N = int(input())

dic = {}
all = {i : i for i in range(1, 20 + 1)}

for i in range(N):
    item = tuple(sys.stdin.readline().split())
    
    if item[0] == 'add':
        dic[int(item[1])] = int(item[1])
        
    elif item[0] == 'remove':
        if int(item[1]) in dic:
            del dic[int(item[1])]
        
    elif item[0] == 'check':
        if int(item[1]) in dic:
            print(1)
        else :
            print(0)
            
    elif item[0] == 'toggle':
        if int(item[1]) in dic:
            del dic[int(item[1])]
        else :
            dic[int(item[1])] = int(item[1])
        
    elif item[0] == 'all':
        dic = all.copy()
    else :
        dic = {}
    
        
    




    