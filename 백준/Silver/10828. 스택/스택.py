import sys

class myStack :
    def __init__(self) :
        self.data = []
        self.size = 0
        
    def push(self, data):
        self.data.insert(0, data)
        self.size += 1
    
    def isEmpty(self):
        if self.size == 0:
            return 1
        else :
            return 0
    
    def pop(self):
        if self.size == 0:
            return -1
        num = self.data.pop(0)
        self.size -= 1
        return num
    
    def top(self):
        if self.size == 0 :
            return -1
        return self.data[0]
        
N = int(input())
myst = myStack()

question = []

for _ in range(N):
    question.append(sys.stdin.readline().strip())

for item in question:
    if item[0] == 'p':
        if item[1] == 'u':
            _ , n = item.split()
            myst.push(n)
        else:
            print(myst.pop())
        
    elif item[0] == 's':
        print(myst.size)
    elif item[0] == 'e':
        print(myst.isEmpty())
    elif item[0] == 't':
        print(myst.top())