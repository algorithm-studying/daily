import math

def solution(progresses, speeds):
    answer = []
    date = []
    
    for i in range(len(progresses)):
        date.append(math.ceil((100-progresses[i])/speeds[i]))
    
    due = -1
    cnt = 0
    for i in range(len(date)):
        if due < date[i]:
            if(cnt):
                answer.append(cnt)
            due = date[i]
            cnt = 1
        else:
            cnt += 1
    
    answer.append(cnt)
    return answer
