def solution(n):
    answer = ''
    
    for i in range(n):
        if(i == 0 or answer[i-1:i] == '박'):
            answer += '수'
        else:
            answer += '박'
            
    return answer
