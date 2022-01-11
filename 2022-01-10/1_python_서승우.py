def solution(lottos, win_nums):
    answer = [0,0]
    result = [6,6,5,4,3,2,1]
    match_cnt = 0
    
    zero_cnt = lottos.count(0)
    
    for num in lottos:
        if num in win_nums:
            match_cnt += 1
    
    answer[0] = result[match_cnt + zero_cnt]
    answer[1] = result[match_cnt]
    return answer