def solution(w,h):
    a=[w,h]
    i=max(a)
    b=True

    while (b):
        if (max(a)%i==0)and(min(a)%i==0):
            b=False
        else :
            i=i-1
        
    w_l = max(a)/i
    h_l = min(a)/i
    answer =w*h-(w_l+h_l-1)*i
    
    return answer