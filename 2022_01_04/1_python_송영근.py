def solution(sizes):
    w=[]
    h=[]
    for x, y in sizes:
        if x<y:
            x, y = y, x
        w.append(x)
        h.append(y)
    width = max(w)
    height = max(h)
    
    return width*height