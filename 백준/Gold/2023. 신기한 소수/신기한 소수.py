import sys
sys.setrecursionlimit(10000)
import math

# sosu = [2 ,3, 5, 7]
# holsoo = [i for i in range(10) if i % 2 != 0]
# print(holsoo)
N = int(input())

def isSosu(N):
    for i in range(2 , int(N / 2 + 1)):
        if N % i == 0:
            return False
    return True


def DFS(num):    
    # if isSosu(num) : 
    #     if len(str(num)) == N:
    #         print(num)
    #     else :
    #         for item in holsoo :
    #             if isSosu(num * 10 + item ):
    #                 DFS(num * 10 + item)
    # else :
    #     return
    
    if len(str(num)) == N:
        print(num)
        # return
    else :
        for item in range(1, 10) :
            if item % 2 == 0 :
                continue
            if isSosu(num * 10 + item) : 
                DFS(num * 10 + item)
            
        # return
    

DFS(2)
DFS(3)
DFS(5)
DFS(7)
    
    



