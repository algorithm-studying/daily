def solution(sizes):
    max_w = max_h = 0
    for arr in sizes:
        if arr[0] < arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        if arr[0] > max_w:
            max_w = arr[0]
        if arr[1] > max_h:
            max_h = arr[1]
    answer = max_w * max_h
    return answer

    
# for문 돌리기
""" def solution(sizes):
    max_w, max_h = 0, 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    return max_w * max_h """

