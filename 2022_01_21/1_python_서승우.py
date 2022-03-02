def solution(price, money, count):
    total_fee = ((count * (count+1)) / 2) * price
    result = total_fee - money
    return result if result > 0 else 0