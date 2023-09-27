import sys

N, M = map(int ,sys.stdin.readline().split())

dic = {}
answer = []
for _ in range(N):
    dic[sys.stdin.readline().strip()] = 0
    
for _ in range(M):
    person = sys.stdin.readline().strip()
    if person in dic:
        answer.append(person)

answer.sort() 
print(len(answer))
for item in answer:
    print(item)