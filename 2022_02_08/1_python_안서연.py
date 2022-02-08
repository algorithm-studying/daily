def solution(s):
    answer = False
    
    if(len(s) in [4,6] and s.isnumeric()):
        answer = True
    
    return answer
