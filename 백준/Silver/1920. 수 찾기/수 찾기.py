import sys

N = int(input())
data = list(map(int , sys.stdin.readline().split()))
M = int(input())
finding_data = list(map(int, sys.stdin.readline().split()))

data.sort()

def BinarySearch(num):
    left = 0
    right = len(data) - 1
    
    while left <= right :
        mid = (left + right) // 2
        
        if num == data[mid] :
            return True
        
        elif num > data[mid] :
            left = mid + 1
        else :
            right = mid - 1
    
    return False

for item in finding_data:
    if BinarySearch(item):
        print(1)
    else:
        print(0)
            
            
