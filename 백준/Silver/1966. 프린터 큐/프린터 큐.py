import sys
from queue import PriorityQueue
from collections import deque

N = int(input())

def get_answer(count, question, arr):
    myque = PriorityQueue()
    data = deque()
    for i in range(count):
        data.append((arr[i], i))
    
    answer = 1
    while len(data) > 0:
        index = find_max_index(data)
        
        for i in range(index):
            data.append(data.popleft())
        num = data.popleft()

        if num[1] == question :
            return answer
        # print(data)
        answer += 1
        

def find_max_index(arr):
    num = arr[0][0]
    index = 0
    for i in range(len(arr)):
        if num < arr[i][0]:
            num = arr[i][0]
            index = i
    return index        
        


for _ in range(N):
    count, question = map(int, sys.stdin.readline().split())
    priorityData = list(map(int, sys.stdin.readline().split()))
    # myQue = PriorityQueue()
    print(get_answer(count, question, priorityData))
    
        
    
