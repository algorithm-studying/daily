import heapq
def solution(n, works):
    max_heap = []
    for work in works:
        heapq.heappush(max_heap, -work)
    for _ in range(n):
        result = heapq.heappop(max_heap)
        if result != 0:
            heapq.heappush(max_heap, (result + 1))
        else:
            heapq.heappush(max_heap, result)
    return sum([work ** 2 for work in max_heap])