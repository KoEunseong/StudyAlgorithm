import sys
# sys.setrecursionlimit(10**7)

memo = [0,0,1,1]

def makeOne(N):
    global memo
    if N <= 3:
        return memo[N]
    for i in range(4, N + 1):
        data = memo[i - 1]
        if i % 2 == 0 and data > memo[i // 2]:
            data = memo[i // 2]
        if i % 3 == 0 and data > memo[i // 3]:
            data = memo[i // 3]
        memo.append(data + 1)
    return memo[N]
# def makeOne(N):
#     if N in dic:
#         return dic[N]
#     data = []
    
#     if N % 3 == 0:
#         if N // 3 in dic:
#             data.append(dic[N // 3])
#         else :
#             data.append(makeOne(N // 3))
#     if N % 2 == 0:
#         if N // 2 in dic:
#             data.append(dic[N // 2])
#         else:
#             data.append(makeOne(N // 2))
#     if N - 1 in dic:
#             data.append(dic[N - 1])
#     else :
#         data.append(makeOne(N - 1))
    
#     answer = min(data) + 1
#     dic[N] = answer
#     return answer
        
#     # min_data = makeOne(data[0]) + 1
#     # for i in range(1,len(data)):
#     #     if min_data > makeOne(data[i]) + 1:
#     #         min_data = makeOne(data[i]) + 1
            
#     # dic[N] = min_data    
#     # return min_data

N = int(input())
print(makeOne(N))

