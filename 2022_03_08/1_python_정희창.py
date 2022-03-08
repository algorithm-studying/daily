
def solution(s):
    s = s.lower()
    p_n = s.count('p')
    y_n = s.count('y')
    if p_n == y_n or p_n+y_n==0:
        
        return True
    else:
        return False
