from itertools import combinations
def solution(numbers):
    com=list(combinations(numbers,2)) #모든 조합 구하기
    result=[]
    for i in com:
        result.append(sum(i))
    result=set(result) #set으로 중복 제거
    result=list(result)
    result.sort()
    return result
