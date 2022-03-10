# 레벨1_문자열 내 p와 y의 개수

def solution(s):
    answer = True
    s1=s.upper()
    p_cnt=0
    y_cnt=0
    for i in s1:
        if i =='P':
            p_cnt += 1
        elif i == 'Y':
            y_cnt += 1
    if p_cnt != y_cnt:
        answer = False
    return answer
