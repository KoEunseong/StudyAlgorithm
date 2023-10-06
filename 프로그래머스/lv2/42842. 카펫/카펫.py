def solution(brown, yellow):
    
    sumxy = (brown + 4) //2
    mulxy = brown + yellow
    print(sumxy, mulxy)
    
    for i in range(1, (sumxy // 2) + 1):
        x = i
        y = sumxy - x
        if x * y == mulxy:
            break
    x, y = max(x,y),min(x,y)
    return [x, y]
    
    