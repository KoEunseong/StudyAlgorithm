N = int(input())


answer = 0
j = 0
isTrue = False
while True:
    
    item = str(j)
    
    for i in range(len(item) - 2):
        if item[i] == '6' and item[i + 1] == '6' and item[i + 2] == '6':
            answer += 1
            isTrue = True
            break
    
    if answer == N:
        break
    j+= 1
    
print(j)
    