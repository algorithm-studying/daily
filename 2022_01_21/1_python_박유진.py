def solution(price, money, count):
    answer = 0
    repeat = 0
    fee = 0
    for i in range(1, count+1):
        repeat += i
    fee = price * repeat
    if fee < money:
        answer = 0
    else:
        answer = fee-money
    return answer