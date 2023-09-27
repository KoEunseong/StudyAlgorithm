import sys

N = int(input())

stairInfo = [0 for i in range(N + 1)]
answer = [[] for i in range(N + 1)]
for i in range(N):
    stairInfo[N - 1 - i] = int(sys.stdin.readline())
    
answer[0].append((stairInfo[0], 1))
answer[1].append((stairInfo[1] + stairInfo[0], 2))

for i in range(2, N):
    n1 = max(answer[i - 2]) #두칸 전
    answer[i].append((n1[0] + stairInfo[i], 1))
    
    for item in answer[i - 1]: #한칸 전
        if item[1] == 1:
            answer[i].append((item[0] + stairInfo[i], 2))


n1 = max(answer[N - 1])
n2 = max(answer[N - 2])        
answer = max(n1, n2)
print(answer[0])
        
        
        

