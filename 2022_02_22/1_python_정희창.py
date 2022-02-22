def solution(absolutes, signs):
    answer = []
    result = 0
    for bool in signs:
        if bool == True:
            answer.append(1)
        else:
            answer.append(-1)
            
    for x, y in zip(absolutes, answer):
        result += x*y
        
    return result
