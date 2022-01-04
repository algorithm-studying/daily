def solution(sizes):
    answer = 0
    
    for s in sizes:
        if s[0] < s[1]:
            tmp = s[0]
            s[0] = s[1]
            s[1] = tmp
    
    maxw = max([s[0] for s in sizes])
    maxh = max([s[1] for s in sizes])
    
    answer = maxw * maxh
    
    return answer
