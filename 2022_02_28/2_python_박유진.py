import heapq

def solution(scoville, K):
    new = 0
    heapq.heapify(scoville)
    for i in range(1, len(scoville)):
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new = min1 + min2 * 2
        heapq.heappush(scoville, new)
        if scoville[0] >= K: return i
    return -1