import sys

def out(cards):
    if len(cards) == 1:
        return cards
    output = []
    for i in range(1, len(cards),2):
        output.append(cards[i])
    if len(cards) % 2 == 1:
        output.append(output[0])
        del output[0]
    

    return out(output) 
    
    

N = int(input())
cards = [i for i in range(1 ,N + 1)]
output = out(cards)
print(*output)

