# 레벨2_다음 큰 숫자

def solution(n):
    answer = 0
    r_cnt = 0
    for i in bin(n)[2:]:
        if i == '1':
            r_cnt += 1

    while True:
        n += 1
        cnt = 0
        for i in bin(n)[2:]:
            if i == '1':
                cnt += 1
        if r_cnt==cnt:
            break
    answer = n
    return answer
