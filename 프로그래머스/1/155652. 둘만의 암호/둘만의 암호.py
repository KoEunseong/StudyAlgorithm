def solution(s, skip, index):
    answer = ''
    skip = [ord(item) for item in skip]
    
    
    
    for item in s :
        st = ord(item)
        temp = 0
        while temp < index :
            st += 1
            if st > 122 :
                st = 97
            if st in skip:
                continue
            temp += 1
        answer += chr(st)
        
    print(answer)
    return answer
    