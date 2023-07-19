import sys

N = int(sys.stdin.readline())
myCard = list(map(int,sys.stdin.readline().split()))
myCard_dic = {}

for item in myCard:
    if item in myCard_dic:
        myCard_dic[item] += 1
    else :
        myCard_dic[item] = 1
M = int(sys.stdin.readline())

yourCard = list(map(int,sys.stdin.readline().split()))

for item in yourCard:
    if item in myCard_dic:
        print(myCard_dic[item],end = ' ')
    else:
        print(0, end=' ')