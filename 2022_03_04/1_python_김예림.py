def solution(n):
    s="수박"
    if n%2==0:
        return s*(n//2)
    else:
        return s*(n//2)+s[0]
