def solution(n):
    sosu = [True for _ in range(n + 1)]
    sosu[1] = False
    answer = 0
    for i in range(2, len(sosu)):
        if not sosu[i] :
            continue
        answer += 1
        for j in range(i+i, len(sosu), i):
            sosu[j] = False
    return answer