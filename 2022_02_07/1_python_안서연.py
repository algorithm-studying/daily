def solution(arr):
    answer = []
    
    for a in arr:
        if len(answer)>0:
            if a != answer[-1]:
                answer.append(a)
        else:
            answer.append(a)
    
    return answer
