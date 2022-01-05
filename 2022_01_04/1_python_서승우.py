def solution(sizes):
    w = 0
    h = 0
    for width, height in sizes:
        if width < height:
            width, height = height, width
        w = max(w, width)
        h = max(h, height)
    return w*h