# 레벨1_내적

def solution(a, b):
    answer = 0
    for n in range(0, len(a)):
        answer += a[n] * b[n]
    return answer

