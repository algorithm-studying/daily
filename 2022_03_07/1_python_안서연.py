def solution(a, b):
    answer = 0
    li = [a, b]
    li.sort()
    
    for i in range(li[0], li[1]+1):
        answer += i
        
    return answer
