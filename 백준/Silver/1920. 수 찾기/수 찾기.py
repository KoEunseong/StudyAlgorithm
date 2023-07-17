import sys
def binary_Search(data_list, value):
    
    left = 0
    right = len(data_list) - 1
    
    while True:
        mid = (left + right) // 2
        if left > right :
            return 0
        elif data_list[mid] == value:
            return 1
        elif data_list[mid] > value:
            right = mid -1
        elif data_list[mid] < value:
            left = mid + 1 


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

A.sort()
mid = N //2
for i in range(M):
    print(binary_Search(A,data[i]))