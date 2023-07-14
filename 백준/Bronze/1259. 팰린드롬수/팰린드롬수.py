import sys
def ispalindrome(value):
    mid = len(value) // 2
    
    for i in range(mid + 1):
        if value[i] != value[-i - 1]:
            return False
    return True        
    
answer = []
while True:
    s = sys.stdin.readline().strip()
    if int(s) == 0:
        break
    if ispalindrome(s):
        answer.append('yes')
    else :
        answer.append('no')
for i in answer:
    print(i)