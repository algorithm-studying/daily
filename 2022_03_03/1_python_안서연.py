def solution(seoul):
    answer = ''
    
    for idx, person in enumerate(seoul):
        if person == 'Kim':
            answer = f'김서방은 {idx}에 있다'
            break
    
    return answer
