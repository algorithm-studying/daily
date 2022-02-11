def solution(priorities, location):
    answer=0
    while True:
        m=max(priorities)
        for i in range(len(priorities)):
            if priorities[i]==m:
                answer+=1
                priorities[i]=0 #인쇄된것은 0으로
                m=max(priorities)
                if location==i:
                    return answer
