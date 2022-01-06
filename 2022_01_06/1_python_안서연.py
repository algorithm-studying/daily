from itertools import combinations

def solution(nums):
    answer = -1

    comb = list(combinations(nums,3))
    sum_comb = [sum(c) for c in comb]
    
    prime = len(sum_comb)
    for num in sum_comb:
        for i in range(2, num):
            if(num % i == 0):
                prime -= 1
                break
    
    answer = prime
    return answer
