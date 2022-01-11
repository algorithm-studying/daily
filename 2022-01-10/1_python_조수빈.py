# 레벨1_로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    rule = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} # 맞힌 개수 : 등수
    worst=0
    for win_num in win_nums:
        worst+=lottos.count(win_num)
    best=worst+lottos.count(0)

    answer.append(rule[best])
    answer.append(rule[worst])
    return answer
