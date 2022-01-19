def solution(lottos, win_nums):

    cnt_zero = 0
    cnt_same = 0
    
    for i in range(0,6):
        if(lottos[i] == 0):
            cnt_zero += 1
        elif(lottos[i] in win_nums):
            cnt_same += 1
    
    min_win_level = 7 - cnt_same
    max_win_level = 7 - (cnt_same + cnt_zero)

    if (cnt_same == 0):
        min_win_level = 6
    if ((cnt_same + cnt_zero) == 0):
        max_win_level = 6

    answer = [max_win_level,min_win_level]
    return answer

            
lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]         
print(solution(lottos,win_nums))


lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
print(solution(lottos,win_nums))

lottos = [45, 4, 35, 20, 3, 9]	
win_nums =  [20, 9, 3, 45, 4, 35]
print(solution(lottos,win_nums))


