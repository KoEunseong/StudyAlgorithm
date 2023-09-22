import sys

row , col ,B = map(int, sys.stdin.readline().split()) # 3 4

data = []

min_height = 256
max_height = 0

total = 0
for i in range(row):
    l = list(map(int ,sys.stdin.readline().split()))
    total += sum(l)
    if min(l) < min_height :
        min_height = min(l)
    
    if max(l) > max_height :
        max_height = max(l)
    
    data.append(l)


time_data = [-1 for i in range(256 + 1)]

for height in range(min_height, max_height + 1):
    time = 0
    rock = B
    
    for i in range(row):
        for j in range(col):
            if data[i][j] > height: #제거
                a = data[i][j] - height
                time += 2 * a
                rock += a
                
            # elif data[i][j] < height: #쌓기
            else :
                b = height - data[i][j]
                time += b
                rock -= b
    # if rock < 0:
    #     time_data[height] = -1
    # else :
    if rock >= 0:
        time_data[height] = time



answer = time_data[min_height]
answer_index = min_height

for i in range(min_height, max_height + 1):
    if time_data[i] != -1 and time_data[i] <= answer :
        answer = time_data[i]
        answer_index = i

print(answer, answer_index)