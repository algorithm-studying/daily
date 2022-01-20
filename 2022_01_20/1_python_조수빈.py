# 레벨1_예산

def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if i>budget:
            break
        else:
            budget-=i
            answer+=1
    return answer