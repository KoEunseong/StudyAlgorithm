import sys

N = int(input())

people = []
for _ in range(N):
    i = sys.stdin.readline().rstrip().split()
    people.append(i)
people.sort(key = lambda x : int(x[0])) 

for i in range(N):
    print(*people[i])