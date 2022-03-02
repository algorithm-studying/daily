def solution(n):
    cnt, x = 0, 0
    while x!=1 :
        cnt += 1
        x = n % cnt
    return cnt