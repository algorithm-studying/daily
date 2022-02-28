import heapq
def solution(scoville, K):
    cnt = 0
    mixed = 0
    heapq.heapify(scoville)
    if sum(scoville) == 0:
        return -1
    else:
        while scoville[0] <= K:
            if len(scoville) <= 1:
                return -1
            else:
                food1 = heapq.heappop(scoville)
                food2 = heapq.heappop(scoville)
                mixed = food1 + food2 * 2
                heapq.heappush(scoville, mixed)
                cnt += 1
        return cnt