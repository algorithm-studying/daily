def solution(operations):
    answer = []
    li = []
    
    for o in operations:
        val = o.split()
        if val[0] == 'I':
            li.append(int(val[1]))
        elif val[0] == 'D':
            if li:
                if val[1] == '1':
                    li.remove(max(li))
                else:
                    li.remove(min(li))    
        
    if not li:
        answer = [0, 0]
    else:
        answer = [max(li), min(li)]
    return answer
