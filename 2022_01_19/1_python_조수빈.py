# 레벨1_이상한 문자 만들기

def solution(s):
    answer = ''
    k=0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            k=0
        elif k%2 == 0:
            answer += s[i].upper()
            k += 1
        elif k%2 != 0:
            answer += s[i].lower()
            k += 1

    return answer
