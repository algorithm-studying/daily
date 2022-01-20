def solution(d, budget):
    answer = 0
    d.sort()
    
    for data in d:
        budget -= data
        if budget >= 0:
            answer += 1
        else:
            break
            
    return answer
