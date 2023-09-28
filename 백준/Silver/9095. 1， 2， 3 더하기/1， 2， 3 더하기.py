import sys

T = int(input())

answer = [[] for i in range(11 + 1)]

answer[1].append([1])

# answer[2].append([1,1])
# answer[2].append([2])

# answer[3].append([1,1,1])
# answer[3].append([1, 2])
# answer[3].append([2, 1])
# answer[3].append([3])



for i in range(2, 11 + 1):
    
    for j in range(1, i + 1):
        n1 = answer[j] # 1
        n2 = answer[i - j] # 3
        # print('n1',n1)
        # print('n2',n2)
        # print('sum:', n1 + n2 ,end='\n')
        for item1 in n1:
            for item2 in n2:
                num = item1 + item2
                if num not in answer[i]:
                    answer[i].append(num)
                    
    if i < 4 :
        answer[i].append([i])

for _ in range(T):
    a = int(sys.stdin.readline())
    print(len(answer[a]))