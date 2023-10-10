

def solution(nums):
    sosu = [True for i in range(3000 + 1)]
    dic = {}
    sosu[1] = False
    for i in range(2, len(sosu)):
        if sosu[i] == False:
            continue
        dic[i] = i
        for j in range(i+i, len(sosu),i):
            sosu[j] = False
    answer = 0
    
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            for k in range(j + 1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) in dic:
                    answer += 1

    return answer