from itertools import combinations
def solution(nums):
    cnt=0
    combi=list(combinations(nums,3))
    sum_combi=map(sum,combi)
    sum_combi=list(sum_combi)
    for i in  sum_combi:
        for j in range(2,i-1):
            if i%j==0:
                cnt+=1
                break
    answer=len(sum_combi)-cnt
    return answer

