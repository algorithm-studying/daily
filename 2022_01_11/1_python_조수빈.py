# 레벨1_신규 아이디 추천

def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for i in new_id:
        if i.islower() or i.isdigit() or i in ['-', '_', '.']:
           answer += i
        
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # 4단계
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    
    
    '''if answer :
          if answer[0] == '.':
                  answer = answer[1:]
          elif answer[-1] == '.':
                  answer = answer[:-1]
    '''

    # 5단계
    if answer == '' :
        answer = 'a'
        
    # 6단계
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[0:-1]
            
    # 7단계
    while len(answer) <= 2:
        answer = answer + answer[-1]
    return answer




'''def solution(new_id):
    can_use = ['-', '_', '.', '0', '1', '2', '3', '4', ' 5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p ', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for i in new_id:
        for j in can_use:
            if i == j:
                answer += i
    # 3단계
    while True:
        if '..' in answer:
            answer = answer.replace('..', '.')
        else:
            break
    # 4단계
    if answer :
        if answer[0] == '.':
                answer = answer[1:]
        elif answer[-1] == '.':
                answer = answer[:-1]
    # 5단계
    if answer == '' :
        answer = 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[0:-2]
    # 7단계
    while len(answer) <= 2:
        answer = answer + answer[-1]
    return answer
'''
