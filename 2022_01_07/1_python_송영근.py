def solution(N, stages):
    answer=[]
    falt=[]
    for i in range(1,N+1):
        num=0
        denom = 0
        for j in stages:
            if i==j:
                num+=1
                denom+=1
            elif i<j:
                denom+=1
        falt.append([i,num/denom])
    falt.sort(key=lambda x:x[1], reverse=True)
    for i in range(len(falt)):
        answer.append(falt[i][0])

    return answer

#런타임 에러