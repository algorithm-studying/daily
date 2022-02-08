def solution(s):
    answer = False
    tmp = []
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if 48 <= ord(i) <= 57:
                tmp.append(i)
    
    if len(s) == len(tmp):
        answer = True
    
    return answer

'''
다른 사람 풀이:

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("a234") )
print( alpha_string46("1234") )
'''