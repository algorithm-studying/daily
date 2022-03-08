def solution(s):
    s = s.lower()
    p = []
    y = []
    for alpa in s:
        if alpa == 'p':
            p.append(alpa)
        elif alpa == 'y':
            y.append(alpa)
            
    return True if len(p) == len(y) else False
'''
다른 사람 풀이:
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )
'''