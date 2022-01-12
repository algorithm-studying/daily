# def solution(n, times):
#     answer = 0
#     times.sort()
#     check1 = [0 for i in range(len(times))]
    
#     idx = 0
#     while(n > 0):
#         if(n == 1):
#             check2 = check1.copy()
#             for i in range(len(times)):
#                 check2[i] += times[i]
#             break
#         check1[idx] += times[idx]
#         idx = check1.index(min(check1))
#         n -= 1
    
#     idx = check2.index(min(check2))
#     check1[idx] += times[idx]
#     answer = max(check1)

#     return answer


def solution(n, times):
    answer = 0
    
    minimum = 1
    maximum = max(times) * n
    
    while(minimum < maximum):
        mid = (minimum + maximum) // 2 
        
        total = 0
        for t in times:
            total += mid // t
            
        if(total >= n):
            maximum = mid
        else:
            minimum = mid + 1
    
    answer = minimum
    return answer
