import sys
input = sys.stdin.readline()

    
expression = input.strip().split('-')

if expression[0] == '':
    expression[0] = 0

first = 0
new_list = []
for item in expression :
    data = list(map(int , item.split('+')))
    
    new_list.append(sum(data))


if len(expression) == 1:
    for item in new_list :    
        first += item
else :
    first = new_list.pop(0)
    for item in new_list :    
        first -= item

    
# else :
#     # first = int(expression[0])
#     for i in range(1, len(expression)):
#         data = list(map(int, expression[i].split('+')))
#         first -= sum(data)

print(first)