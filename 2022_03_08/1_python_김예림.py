def solution(s):
    s=s.lower()
    if s.count('p')+s.count('y')==0:
        return True
    else:
        if s.count('p')==s.count('y'):
            return True
        else:
            return False
