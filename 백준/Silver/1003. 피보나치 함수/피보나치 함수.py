import sys
dic = {
    0:(0,1,0),
    1:(1,0,1)
}

def fib(n):
    if n in dic:
        return dic[n]
    else :
        sum1 = tuple(sum(i) for i in zip(fib(n-1), fib(n-2)))
        dic[n] = sum1
        return sum1
    

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

for item in numbers:
    t = fib(item)
    print(t[1],t[2])