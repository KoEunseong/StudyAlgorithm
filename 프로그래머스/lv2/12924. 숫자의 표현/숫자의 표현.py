def solution(n):
    answer = 1
    
    for i in range(1, (n // 2) + 1):
        hap = 0
        temp = i
        while True :
            hap += temp
            if hap >= n:
                if hap == n:
                    answer += 1
                break
            temp += 1
    
    return answer