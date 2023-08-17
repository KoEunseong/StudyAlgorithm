import sys
def QuickSort(data, K, start, end):
    pivot = data.pop(end + 1)
    # start = 0
    # print(pivot)
    
    while start < end :
        if data[start] < pivot : 
            start += 1

        if data[end] > pivot : 
            end -= 1
        
        if data[start] > pivot and data[end] < pivot :
            temp = data[start]
            data[start] = data[end]
            data[end] = temp
            start += 1
            end -= 1
    # data.insert(start + 1, pivot)
    
    # print(start)
    if data[start] > pivot :
        data.insert(start, pivot)
        
    elif data[start] < pivot:
        start += 1
        data.insert(start, pivot)
    
    # print(data)
    # print(start)
    if start == K - 1 :
        return pivot
    elif start > K - 1 :
        # print('esens')
        QuickSort(data, K, 0, start - 2)
    else : 
        # print('sense')
        QuickSort(data, K, start + 1, len(data) - 2)
        
        
    
    
    
        
    

N,K = map(int,sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))
# print(data)
# QuickSort(data,K, 0, len(data) - 2)
# print(data)
data.sort()
print(data[K - 1])