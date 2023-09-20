import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())


data = [i for i in range(N + 1)]

def union(n1, n2):
    if n1 != data[n1]:
        union(data[n1] , n2)
    elif n2 != data[n2]:
        union(n1 , data[n2])
    else :
        data[n2] = n1
        # print(data)

def find(n1):
    
    # if n1 == n2 :
    #     return n1
    
    if n1 == data[n1]: #대표 노드
        return n1
    
    else :
        result = find(data[n1])
        data[n1] = result
    
    return result

for _ in range(M):
    a, b, c = map(int ,sys.stdin.readline().split())
    
    if a == 0 :
        if b > c :
            b, c = c, b
        union(b , c) # 작은 수 , 큰 수

    else :
        b1 = find(b)
        b2 = find(c) # 대표 메뉴가 같으면 그거는 같은집합
        
        # print(b1, b2)
        # print(data)
        if b1 == b2 :
            print('YES')
        else :
            print('NO')
    
