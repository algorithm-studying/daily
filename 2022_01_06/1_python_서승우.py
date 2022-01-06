from itertools import combinations
import math
def solution(nums):
    answer = 0
    combi = list((combinations(nums, 3))) # 3개의 수를 선택하는 조합 구하기
    for i in range(len(combi)):
        for j in range(2, int(math.sqrt(sum(combi[i])))+1): # 각 조합의 합이 소수인지 판별
            if sum(combi[i]) % j == 0:
                answer += 1
                break
    return len(combi) - answer