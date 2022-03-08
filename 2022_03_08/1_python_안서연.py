def solution(s):
    cp = s.count('p') + s.count('P')
    cy = s.count('y') + s.count('Y')
    
    if cp == cy or cp+cy == 0:
        return True
    else:
        return False
