def solution(s):
    answer = True
    
    stack = []
    
    for i in range(len(s)):
        item = s[i]
        if item == '(':
            stack.append(item)
        else :
            if len(stack) == 0:
                answer = False
                break
            else :
                stack.pop()
        
    
    if len(stack) != 0:
        answer = False
    return answer