def solution(n):
    n_3=""
    while n:
        n_3 += str(n%3)
        n=n//3
        
    answer = int(n_3,3)
    return answer