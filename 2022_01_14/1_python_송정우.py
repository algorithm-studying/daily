def solution(n, lost, reserve):
    tmp = [1] * n
    
    for i in lost:
        tmp[i - 1] -= 1
    
    for i in reserve:
        tmp[i - 1] += 1
    
    for i, v in enumerate(tmp):
        if v == 2:
            if (i - 1 >= 0) and (tmp[i - 1] == 0):
                tmp[i - 1] += 1
                tmp[i] -= 1
            elif (i + 1 < n) and (tmp[i + 1] == 0):
                tmp[i + 1] += 1
                tmp[i] -= 1
            else:
                tmp[i] -= 1
    
    if sum(tmp) >=  n:
        return n
    else:
        return sum(tmp)

'''
다른 사람 풀이:

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
'''