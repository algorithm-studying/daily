def solution(prices):
    answer = []
    for i in range(len(prices) - 1): # 마지막은 항상 0
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            elif prices[i] > prices[j]:
                cnt += 1  # 떨어져도 1초동안은 가격이 안 떨어진 걸로 봄
                break
        answer.append(cnt)
    answer.append(0)  # 마지막은 항상 0
    
    return answer

'''
다른 사람 풀이:   cf) deque를 쓰는 게 효율성 테스트에서 2배정도 빠름

from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer
'''