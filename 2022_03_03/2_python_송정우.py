def solution(brown, yellow):
    divisor = []
    answer = []
    tot_size = brown + yellow
    for i in range(1, tot_size + 1):
        if tot_size % i == 0:
            divisor.append(i)
            
    for n in divisor:
        set_n = int(tot_size / n)  # 가로, n = 세로
        if (set_n - 2) * (n - 2) == yellow:
            answer.append(set_n)
            answer.append(n)
            break
    
    return answer