import sys
# def size_ranking(people):    
#     rank = 1
#     same = 1
#     for i in range(len(people)):
#         if i == len(people) - 1:
#             people[i].append(rank)
#         elif people[i][1] >= people[i + 1][1]:
#             people[i].append(rank)
#             rank += same
#             same = 1
#         else:
#             people[i].append(rank)
#             same += 1
            
#         # elif people[i][0] == people[i + 1][0]:
#         #     if people[i][1] == people[i + 1][1]:
#         #         people[i].append(rank)
#         #         same += 1
#         #     else :
#         #         people[i].append(rank)
#         #         rank += same
#         #         same = 1
#         # else:
#         #     if people[i][1] >= people[i + 1][1]:
#         #         people[i].append(rank)
#         #         rank += same
#         #         same = 1
#         #     else :
#         #         people[i].append(rank)
#         #         same += 1
                
                

N = int(input())
people = []
for i in range(N):
    w,h = map(int, sys.stdin.readline().split())
    people.append((w,h))
# people.sort(key = lambda x: (x[0], x[1]),reverse=True)
# size_ranking(people)
# print(people)


for item in people:
    rank = 0
    for i in people:
        if item[0] < i[0] and item[1] < i[1]:
            rank += 1
    
    print(rank + 1,end=' ')