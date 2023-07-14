n = int(input())
line = input()
list_a = line.split(' ')
list_a = list(map(lambda x : int(x) , list_a))

# print(n)
# print(line)
# print(list_a)
count = n

for i in list_a:
    if i == 1 :
        count -= 1
        continue
    for j in range(2, i):
        if i % j == 0:
            count -= 1
            break
        
print(count)