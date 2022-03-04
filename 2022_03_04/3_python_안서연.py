# from itertools import combinations
# def solution(n):
#     answer = 0
#     li = []
    
#     for _ in range(n // 2):
#         li.append(2)
#     for _ in range(n % 2):
#         li.append(1)
#     ans = list(combinations(li, li.count(2)))
#     answer += len(ans)
    
#     while(li.count(2) != 0):
#         if li.pop(0) == 2:
#             li.append(1)
#             li.append(1)  
#         ans = list(combinations(li, li.count(2)))
#         answer += len(ans)
    
#     return answer

def solution(n):
    answer = 0
    li = []
    
    li.append(1)
    li.append(2)
    for i in range(2,n):
        li.append((li[-2]+li[-1])%1000000007)
    
    answer = li[-1]
    return answer
