def solution(s):
    number = ['0','1','2','3','4','5','6','7','8','9']
    answer = True
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i] not in number:
                answer = False
    else:
        answer = False
    return answer

#다른 사람 코드
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)