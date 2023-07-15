import sys
n = int(sys.stdin.readline())

words = []
for _ in range(n):
    words.append(sys.stdin.readline().strip()) #sys롤 문자열을 읽어들일때 꼭 strip해줘야함

words = list(set(words))    
words.sort(key=lambda x: (len(x), x))

for item in words:
    print(item)