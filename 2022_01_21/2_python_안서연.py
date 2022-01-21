def solution(n):
    answer = 0
    next_n = n + 1
    cnt_1 = list(bin(n))[2:].count('1')
    
    while(1):
        if(list(bin(next_n))[2:].count('1') == cnt_1):
            answer = next_n
            break
        next_n += 1
    
    return answer
