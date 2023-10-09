import math
def solution(n):
    ans = 0
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    n = bin(n)
    # print(n.count('1'))
    return n.count('1')
#     while n != 1:
#         n /= 2
#         if n != int(n):
#             cnt += 1
#             n = math.floor(n)
    
#     return cnt