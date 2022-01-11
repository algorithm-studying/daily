def solution(lottos, win_nums):
    answer = []
    
    zero_cnt = 0
    cnt = 0
    for l in lottos:
        if l == 0:
            zero_cnt += 1
        else:
            if l in win_nums:
                cnt += 1
    
    if cnt+zero_cnt >= 2:
        answer.append(7-(cnt+zero_cnt))
    else:
        answer.append(6)
    
    if cnt >= 2:
        answer.append(7-cnt)
    else:
        answer.append(6)

    return answer
