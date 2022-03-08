def solution(a,b):
    if a > b: # a, b 크기 순대로 나열
        a, b = b, a
    return (b*(b+1) / 2) - ((a-1)*(a) / 2) # 1~n까지 합 공식 활용
