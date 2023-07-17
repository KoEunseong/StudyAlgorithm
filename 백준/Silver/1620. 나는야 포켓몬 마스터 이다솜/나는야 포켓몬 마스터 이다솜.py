import sys
        
N,M = map(int, sys.stdin.readline().split())

dogam = []
dogam_s = {}
question = []
for i in range(N):
    poketmon = sys.stdin.readline().strip()
    dogam.append((i ,poketmon))
    dogam_s[poketmon] = i

for i in range(M):
    question.append(sys.stdin.readline().strip())

for item in question:
    if item.isdigit():
        print(dogam[int(item) - 1][1])
    else :
        print(dogam_s[item] + 1)
