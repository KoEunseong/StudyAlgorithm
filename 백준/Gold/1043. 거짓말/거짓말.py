import sys
input = sys.stdin

N, M = map(int , input.readline().split())

party = []
people = [i for i in range(N + 1)]
truth_people = list(map(int, input.readline().split()))
def union(n1, n2):
    a = find(n1)
    b = find(n2)
    
    if a != b:
        people[b] = a
        
def find(num):
    if num == people[num]:
        return num
    else :
        people[num] = find(people[num])
        return people[num]

for i in range(M):
    party.append(list(map(int, sys.stdin.readline().split())))


for i in range(M): # 0 1 2 3
    for j in range(1, len(party[i]) - 1):
        union(party[i][j] , party[i][j + 1])

truth_people.pop(0)

temp = []
for i in range(len(truth_people)):
    temp.append(find(truth_people[i]))
truth_people = temp

answer = M

for i in range(M):
    item = party[i]
    
    for j in range(1 , item[0] + 1):
        if find(item[j]) in truth_people :
            answer -= 1
            break
print(answer)