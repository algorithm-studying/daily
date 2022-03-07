def solution(a, b):
    start=min(a,b)
    end=max(a,b)
    if a==b:
        return a
    else:
        return sum(range(start,end+1))
