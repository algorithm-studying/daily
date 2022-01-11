def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    isDot = False
    for n in new_id:
        if(n.isalpha() or n.isnumeric()):
            isDot = False
            answer += n
        elif(n == '-' or n == '_'):
            isDot = False
            answer += n
        elif(n == '.'):
            if(isDot == True):
                continue
            isDot = True
            answer += n
            continue
    
    answer = answer.strip('.')
    
    if(answer == ''):
        answer += 'a'
    
    if(len(answer) >= 16):
        answer = answer[0:15]
        if(answer[14] == '.'):
            answer = answer[:-1]
    
    while(len(answer) < 3):
        answer += answer[-1]
    
    return answer
