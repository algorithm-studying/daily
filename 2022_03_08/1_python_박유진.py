def solution(s):
    s = s.lower()
    num_p = s.count('p')
    num_y = s.count('y')
    if num_p == num_y:
        return True
    elif num_p== 0 and num_y == 0:
        return True
    else: return False