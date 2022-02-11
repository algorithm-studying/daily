def solution(priorities, location):
    answer = 0 
    data = [(p,i) for i,p in enumerate(priorities)]
    
    while(data):
        maximum = max(data)[0]
        check = data.pop(0)
        if(check[0] == maximum):
            answer += 1
            if(check[1] == location):
                break
        else:
            data.append(check)
    
    return answer
