import sys

dic = {
    0:1,
    1:1
}
def fact(N):
    if N in dic:
        return dic[N]
    output = N * fact(N - 1)
    dic[N] = output
    return output
    


N,K = map(int, sys.stdin.readline().split())

print(fact(N) // (fact(K) * fact(N - K)))