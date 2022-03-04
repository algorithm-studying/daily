def solution(n):
    answer = '수박'
    ans='수'

    
    if n % 2 == 0:
        answer = answer*(n//2)
    else:
        answer = answer*(n//2) + ans
        
    return answer


def solution(n):
    
    return "수박"*(n//2) + "수"*(n%2)
