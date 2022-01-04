def solution(sizes):
    w_max=0
    h_max=0
    for x,y in sizes: 
        if x>y:
            x,y=y,x
        w_max=max(w_max,x)
        h_max=max(h_max,y)
    return w_max*h_max