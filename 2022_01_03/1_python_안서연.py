def solution(numbers):
    answer = -1
    
    all = [0,1,2,3,4,5,6,7,8,9]
    none = [a for a in all if a not in numbers]
    answer = sum(none)
    
    return answer
