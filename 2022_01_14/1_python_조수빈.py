# 레벨1_체육복

# 전체 학생의 수 n,
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve

def solution(n, lost, reserve):
    answer = 0
    reserve.sort()
    lost.sort()
    import copy
    lost_2 = copy.copy(lost)
    reserve_2= copy.copy(reserve)
    for i in lost_2:
        if i in reserve_2:
            lost.remove(i)
            reserve.remove(i)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    answer = n - len(lost)
    return answer


'''def solution(n, lost, reserve):
    answer = 0

    set_lost = list(set(lost) - set(reserve))
    set_reserve = list(set(reserve) - set(lost))

    answer= n-len(set_lost)

    for i in set_lost:
        if i in set_reserve:
            set_reserve.remove(i)
            answer += 1

        elif i-1 in set_reserve:
            set_reserve.remove(i-1)
            answer += 1

        elif i+1 in set_reserve:
            set_reserve.remove(i+1)
            answer += 1

    return answer'''

