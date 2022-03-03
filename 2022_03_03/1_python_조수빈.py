# 레벨1_서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    cnt=0
    for person in seoul:
        if person=='Kim':
            break
        cnt+=1
    answer= f'김서방은 {cnt}에 있다'
    return answer