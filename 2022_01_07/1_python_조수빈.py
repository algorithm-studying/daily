# 레벨1_실패율


def solution(N, stages):
    user = len(stages)
    failure = {}
    for i in range(1, N + 1):
        if user != 0:
            failure[i] = stages.count(i) / user # failure 딕셔너리에 i스테이지, i실패율 저장
            user -= stages.count(i)
        else:
            failure[i] = 0

    return sorted(failure, key=lambda i: failure[i], reverse=True)


''' 런타임에러
import operator

def solution(N, stages):
    answer = []
    failure={}
    i=1
    while i < N+1:
        cnt = 0
        cnt_on = 0
        for j in stages:
            if j >= i:
                cnt += 1 # 스테이지에 있는 유저수
            if j == i:
                cnt_on += 1  # 스테이지에 머무는 유저수
        failure[i] = cnt_on/cnt # i번째 스테이지의 실패율
        i+=1
    answer = sorted(failure.items(), key=lambda x: x[1], reverse=True)

    return answer
'''