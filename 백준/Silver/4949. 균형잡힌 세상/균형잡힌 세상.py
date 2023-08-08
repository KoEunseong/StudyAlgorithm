import sys

data = []
while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == '.':
        break
    data.append(sentence)


for item in data:
    stack = []
    for i in item:
        if i == '(':
            stack.append('(')
            
        elif i == '[':
            stack.append('[')
            
        elif i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                stack.append(-1)
                break
            stack.pop()
            
        elif i == ']':
            if len(stack) == 0 or stack[-1] != '[':
                stack.append(-1)
                break
            stack.pop()
            
    if len(stack) != 0:
        print('no')
    else : 
        print('yes')
    