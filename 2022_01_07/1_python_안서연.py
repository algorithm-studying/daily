def solution(N, stages):
    answer = []
    fail_rate = []
    
    for i in range(1,N+1):
        challenge = 0
        fail = 0
        for s in stages:
            if(s >= i):
                challenge += 1
                if(s == i):
                    fail += 1
        if(challenge == 0):
            fail_rate.append([0, i])
        else:
            fail_rate.append([fail/challenge, i])
    
    fail_rate.sort(key=lambda x:(-x[0],x[1]))
    answer = [f[1] for f in fail_rate]
    
    return answer
