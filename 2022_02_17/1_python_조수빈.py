# 레벨1_음양 더하기

def solution(absolutes, signs):
    answer = 0
    for num in range(0,len(absolutes)):
        if signs[num] == True:
            answer += absolutes[num]
        else:
            answer -= absolutes[num]
    return answer
