def solution(numer1, denom1, numer2, denom2):
    
    a = denom1* numer2 + denom2*numer1
    b = denom1 * denom2
    
    c = max(a,b)
    d = min(a,b)
    
    while d != 0:
        c, d = d ,c % d
    
    return [a // c, b //c]
        
    
    

        
        