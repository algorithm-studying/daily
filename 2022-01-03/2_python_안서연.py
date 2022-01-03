def func(w,h):
    a, b = max([w,h]), min([w,h])
    while(True):
        c = a % b
        if c == 0:
            return b
        a = b
        b = c

def solution(w,h):
    answer = 1
    
    all = w*h
    gcd = func(w,h)
    answer = all - (w+h-gcd)
    
    return answer
