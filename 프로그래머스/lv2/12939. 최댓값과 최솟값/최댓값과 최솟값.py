def solution(s):
    data = list(map(int, s.split()))
    n1 = min(data)
    n2 = max(data)
    answer = str(n1) + ' ' + str(n2)
    
    return answer