def solution(progresses, speeds):
    answer = []
    
    while len(progresses) != 0:
        cnt = 0 #배포될 progress의 수 count
        
        # speed에 맞게 progress 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        # 100%를 달성한 progress는 배포진행
        while (len(progresses) > 0 and progresses[0] >= 100):
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        
        if cnt > 0: 
            answer.append(cnt)
            
    return answer