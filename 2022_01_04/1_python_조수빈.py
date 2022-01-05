def solution(sizes):
    answer = 0
    sizes = [sorted(size, reverse=True) for size in sizes]
    # size : 앞에 더 긴 길이가 오도록 정렬
    w = [size[0] for size in sizes]
    h = [size[1] for size in sizes]
    answer = max(w) * max(h)
    return answer