# 레벨1_문자열 다루기 기본

def solution(s):
    answer = False
    if len(s)==4 or len(s)==6:
        for ss in s:
            if ss in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                answer = True
            else:
                answer = False
                break
    return answer

