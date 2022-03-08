def solution(s):
    s = s.lower()
    p_n = s.count('p')
    y_n = s.count('y')
    return p_n == y_n
