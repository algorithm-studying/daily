import heapq

def solution(scoville, K):
    cnt = 0
    
    heapq.heapify(scoville)
    min_sco = heapq.heappop(scoville)
    
    while (len(scoville)) and (min_sco < K):
        sco = heapq.heappop(scoville)
        if min_sco >= sco:
            new_food = sco + (min_sco * 2)
        else:
            new_food = min_sco + (sco * 2)
        heapq.heappush(scoville, new_food)
        cnt += 1
        min_sco = heapq.heappop(scoville)
    
    if (min_sco < K) and not len(scoville):
        cnt = -1
        
    return cnt