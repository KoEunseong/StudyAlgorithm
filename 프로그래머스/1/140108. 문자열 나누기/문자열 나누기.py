def solution(s):
    answer = 0
    
    while s:
        answer += 1
        x = s[0]
        cnt1 = 0
        cnt2 = 0
        for i in range(len(s)):
            if s[i] == x:
                cnt1 += 1
            else :
                cnt2 += 1
            if cnt1 == cnt2 :
                break
        s = s[i + 1:]
        
    print(answer)
    return answer

    