def solution(nums):
    num=len(nums)//2 #가질 수 있는 폰켓몬 갯수
    n=set(nums)
    if num<len(n):
        return num
    else:
        return len(n)
