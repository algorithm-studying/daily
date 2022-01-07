def solution(N, stages):
    fail = {}
    now_stage = [0] * (N + 2)
    
    # 각 스테이지 별 도전 인원 수
    for stage in stages:
        now_stage[stage] += 1

    #스테이지 별 실패율 계산
    for i in range(1,N+1):
        if sum(now_stage[i:]) == 0:
            fail[i] = 0
        else:
            fail[i] = now_stage[i] / sum(now_stage[i:])

    #딕셔너리 정렬 후 반환
    return sorted(fail, key=lambda x: fail[x], reverse=True)