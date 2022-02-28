def solution(left, right):
    answer = 0
    divisor_n = 0
    for i in range(left, right+1):
        divisor_n = 0
        for j in range(1, i+1):
            if i % j == 0:
                divisor_n += 1
        if divisor_n % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer