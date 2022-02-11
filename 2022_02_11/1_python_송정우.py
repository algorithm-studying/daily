def solution(s):
    answer = ''
    if len(s) % 2 != 0:
        answer = s[len(s)//2]
    else:
        answer = s[len(s)//2 -1] + s[len(s)//2]
    return answer
'''
다른 사람 풀이:
def string_middle(str):
    
    return str[(len(str)-1)//2:len(str)//2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))
'''