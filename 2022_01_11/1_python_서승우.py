def solution(new_id):
    answer = ''
    #1단계
    new_id = new_id.lower()
    #2단계
    for word in new_id:
        if word in '_-.' or word.isalnum():
            answer += word
    #3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4단계
    if answer == '.' or answer == '':
        answer = ''
    else:
        if answer[0] == '.':
            answer = answer[1:]
            print(answer)
        if answer[-1] == '.':
            answer = answer[:-1]
    #5단계
    if answer == '':
        answer = 'a'
    #6단계
    if len(new_id) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    #7단계
    if len(answer) <= 2:
        answer = answer + answer[-1] * (3-len(answer))
    return answer