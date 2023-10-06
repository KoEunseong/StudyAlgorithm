import sys
sys.setrecursionlimit(10**6)

dic = {
    0:0, 1:1
}
def fib(n):
    if n in dic :
        return dic[n]
    dic[n] = fib(n - 1) + fib(n - 2)
    
    return dic[n]

def solution(n):
    return fib(n) % 1234567



    