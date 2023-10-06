def solution(n, words):
    
    people = [0 for _ in range(n)]
    dic = {}
    answer = [0, 0]
    
    
    cnt = 0
    
    dic[words[0]] = words[0]
    
    for i in range(1, len(words)):
        item = words[i]
        
        if item in dic or item[0] != words[i -1][-1]:
            print(i)
            answer = [(i % n) + 1, (i // n) + 1]
            break
        dic[item] = item
        
    print(answer)
        
    
    

    return answer