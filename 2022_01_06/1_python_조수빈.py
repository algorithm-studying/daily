# 레벨1_소수 만들기
import itertools

def solution(nums):
    answer=0
    list_threenum = list(itertools.combinations(nums, 3))
    for x in list_threenum:
        sum_threenum = sum(x)

        for y in range(2,sum_threenum):
            if sum_threenum % y == 0:
                break

        else:
            answer += 1
    return answer
