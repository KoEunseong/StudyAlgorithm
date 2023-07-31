import sys

N = int(input())

set_data = set()
all_set = set(str(i) for i in range(1,20 + 1))

for _ in range(N):
    
    line = sys.stdin.readline().strip()
    if line == 'all':
        set_data = all_set
        continue
    if line == 'empty':
        set_data = set()
        continue
    
    op, num = line.split()
    
    
    if op == 'add':
        set_data.add(num)
    elif op == 'remove':
        if num in set_data:
            set_data.remove(num)
        else :
            continue
        
    elif op == 'check':
        if num in set_data:
            print(1)
        else :
            print(0)
    elif op == 'toggle':
        if num in set_data:
            set_data.remove(num)
        else :
            set_data.add(num)
    
    