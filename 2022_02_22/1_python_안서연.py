def solution(absolutes, signs):
    answer = 0
    
    for i, a in enumerate(absolutes):
        if not signs[i]:
            a -= 2*a
        answer += a
    
    return answer
