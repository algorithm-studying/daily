def solution(d, budget):
    d.sort()
    total=0
    if(d[0]>budget): 
        return 0
    for i in range(0,len(d)):
        total+=d[i]
        if total>budget:
            break
        answer=i+1
    return answer
