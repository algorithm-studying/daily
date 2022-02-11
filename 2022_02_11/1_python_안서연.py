def solution(s):
    answer = ''
    length = len(s)
    
    li = list(s)
    if(length%2 == 0):
        answer = li[length//2-1]+li[length//2]
    else:
        answer = li[length//2]
        
    return answer
