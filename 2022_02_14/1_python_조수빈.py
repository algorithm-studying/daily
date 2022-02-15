# 레벨1_폰켓몬

def solution(nums):
    answer = 0
    nums_set=set(nums)
    if len(nums_set) > (len(nums)/2):
        answer=int(len(nums)/2)
    else:
        answer=len(nums_set)
    return answer
