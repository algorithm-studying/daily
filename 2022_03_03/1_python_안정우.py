def solution(seoul):
    answer = ''
    idx = 0
    for i in seoul:
        if (i=='Kim'):
            break
        idx+=1
    return f'김서방은 {idx}에 있다'
