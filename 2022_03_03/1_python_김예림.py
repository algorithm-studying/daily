def solution(seoul):
    answer=''
    for i,str in enumerate(seoul):
        if str=='Kim':
            answer="김서방은 "+f'{i}'+"에 있다"
            return answer
