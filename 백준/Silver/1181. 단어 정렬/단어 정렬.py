import sys
n = int(sys.stdin.readline())

words = []
for _ in range(n):
    words.append(sys.stdin.readline().strip()) #sys롤 문자열을 읽어들일때 꼭 strip해줘야함
    
words.sort(key=lambda x: (len(x), x))
i = 0
for _ in range(n):
    if i > len(words) - 2:
        break
    if words[i] in words[i+1:]:
        words.pop(i)
        continue
    i += 1
    
for item in words:
    print(item)