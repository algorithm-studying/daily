# 레벨1_핸드폰 번호 가리기

def solution(phone_number):
    answer = ''
    l_phone_number=list(phone_number)
    for i in range(0,len(phone_number)-4):
        l_phone_number[i]= '*'
    answer = ''.join(l_phone_number)
    return answer

