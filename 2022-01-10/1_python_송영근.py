def solution(lottos, win_nums):
    correct=0
    rnk=[6, 6, 5, 4, 3, 2, 1]
    for i in win_nums:
        if lottos.count(i)!=0:
            correct+=1
    
    min=rnk[correct]
    max=rnk[correct+lottos.count(0)]  
    
    answer = [max, min]
    return answer