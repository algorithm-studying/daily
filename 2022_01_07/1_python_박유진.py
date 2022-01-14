def solution(N, stages):
    answer = {}
    challengers = len(stages)
    
    for i in range(1, N+1):
        
        if challengers != 0:
            
            loser = stages.count(i)
            answer[i] = loser / challengers
            challengers -= loser
            
        else:
            answer[i] = 0
        
        
    return sorted(answer, key = lambda x: answer[x], reverse = True)