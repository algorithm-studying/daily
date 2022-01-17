def solution(x):
    num=list(map(int,str(x)))
    s=0
    for i in num:
        s+=i
    if x%s==0:
        return True
    else:
        return False
