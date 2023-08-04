import sys

slen, plen = map(int , sys.stdin.readline().split())

DNA = ['A','C','G','T']

data_str = sys.stdin.readline().rstrip()
a,c,g,t = map(int, sys.stdin.readline().split())

i = 0
j = plen - 1
count = 0

window = data_str[i:j + 1]
# window_count = [window.count('A'), window.count('C'), window.count('G'), window.count('T')]

dic = {
    'A' : window.count('A'),
    'C' : window.count('C'),
    'G' : window.count('G'),
    'T' : window.count('T')
}

while j < slen:
    
    if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
        count += 1
    
    dic[data_str[i]] -= 1
    i += 1
    j += 1
    if j < slen:
        dic[data_str[j]] += 1
print(count)
    
