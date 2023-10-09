import math
def solution(arr):
    num = 1
    for i in range(len(arr) - 1):
        arr[i + 1] = arr[i] * arr[i + 1] // math.gcd(arr[i], arr[i + 1])
        
    
    return arr[-1]

        