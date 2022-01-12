def solution(lottos, win_nums):
    answer = []
    possible = []
    
    win = 0
    for i in lottos:
        if i in win_nums:
            win += 1
    
    possible.append(win)
    
    
    win += lottos.count(0)
    
    possible.append(win)
    
    for i in possible: 
        if i == 6 : answer.append(1)
        elif i == 5 : answer.append(2)
        elif i == 4 : answer.append(3)
        elif i == 3 : answer.append(4)
        elif i == 2 : answer.append(5)
        else: answer.append(6)
        
    answer.sort()
    return answer