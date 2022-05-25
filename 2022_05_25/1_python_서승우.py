from itertools import combinations
def solution(numbers):
    count = list(combinations(numbers, 2))
    answer = []
    for nums in count:
        answer.append(sum(nums))
    answer = list(set(answer))
    answer.sort()
    return answer