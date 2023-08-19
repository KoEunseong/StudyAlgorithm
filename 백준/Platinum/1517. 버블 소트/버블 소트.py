import sys


result = 0

# def bubbleSort(data):
#     result1 = 0

#     for i in range(N):
#         for j in range(N - i - 1):
#             if data[j] > data[j + 1]:
#                 data[j], data[j + 1] = data[j + 1], data[j]
#                 result1 += 1
#     return result1

def mergeSort(s, e):
    global result
    if e - s < 1:
        return
    # m  = int((s + e) / 2)
    m = int(s + (e - s) / 2)
    mergeSort(s, m)
    mergeSort(m + 1, e)
    
    for i in range(s, e + 1):
        tmp[i]  = arr[i]
    
    k = s
    i = s
    j = m + 1
    
    while i <= m and j <= e:
        if tmp[i] > tmp[j]:
            arr[k] = tmp[j]
            result += (j - k)
            j += 1
            k += 1
        else :  
            arr[k] = tmp[i]
            i += 1
            k += 1
        
    
    while i <= m:
        arr[k] = tmp[i]
        i += 1
        k += 1
    
    while j <= e:
        arr[k] = tmp[j]
        j += 1
        k += 1

N = int(input())

arr = [0] + list(map(int, sys.stdin.readline().split()))

tmp =  [0] * (N + 1)

mergeSort(1, N)

print(result)
