def solution(nums):
    answer = list(set(nums))
    n = len(answer)
    t = len(nums)
    if n > t//2:
        return t//2
    else:
        return n
