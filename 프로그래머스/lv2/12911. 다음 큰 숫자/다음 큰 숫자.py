def solution(n):
    
    num = n
    cnt1 = str(bin(num)).count('1') 
    
    while True:
        num += 1
        cnt2 = str(bin(num)).count('1') 
        if cnt1 == cnt2:
            break
    
    return num