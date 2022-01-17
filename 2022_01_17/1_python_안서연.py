def solution(x):
    answer = False
    
    li_x = list(map(int, str(x)))
    if(x % sum(li_x) == 0):
        answer = True
        
    return answer
