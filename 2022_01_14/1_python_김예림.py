def solution(n, lost, reserve):
    new_lost=set(lost)-set(reserve)
    new_reserve=set(reserve)-set(lost)
    cnt=len(new_lost)
    for i in new_lost:
        if i-1 in new_reserve:
            cnt-=1
            new_reserve.remove(i-1)
            
        elif i+1 in new_reserve:
            cnt-=1
            new_reserve.remove(i+1)
            
    return n-cnt
        
