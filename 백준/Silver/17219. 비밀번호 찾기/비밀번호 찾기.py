import sys

N,M = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(N):
    site, pw = sys.stdin.readline().split()
    dic[site] = pw


answer = []
for _ in range(M):
    site = sys.stdin.readline().strip()
    # print(dic[site])
    answer.append(dic[site])
for i in range(M):
    print(answer[i])