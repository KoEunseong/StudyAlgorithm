def solution(players, callings):
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i

    for item in callings:
        temp = dic[item]
        dic[players[temp - 1]] += 1
        dic[item] -= 1

        t = players[temp - 1]
        players[temp - 1] = players[temp]
        players[temp] = t

    
    return players

# print(dic.items())