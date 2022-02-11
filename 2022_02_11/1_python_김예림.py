def solution(s):
    answer = ''
    m=len(s)
    if m%2==0:
        answer=s[m//2-1:m//2+1]
    else:
        answer=s[m//2]
    return answer
