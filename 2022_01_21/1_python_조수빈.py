# 레벨1_부족한 금액 계산하기

def solution(price, money, count):
    answer = -1
    real_price = 0
    for cnt in range(1,count+1):
        real_price += price*cnt
        if real_price>money:
            answer = real_price-money
        else:
            answer=0
    return answer
