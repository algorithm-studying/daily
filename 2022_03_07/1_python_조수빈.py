# 레벨1_두 정수 사이의 합

def solution(a, b):
    answer = 0
    c=min(a,b)
    d=max(a,b)
    for num in range(c, d+1):
        answer += num
    return answer
