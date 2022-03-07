def solution(a,b):
    if a > b: # a, b 크기 순대로 나열
        tmp = b
        b = a
        a = tmp
    answer = (b*(b+1) / 2) - ((a-1)*(a) / 2) # 1~n까지 합 공식 활용
    return answer