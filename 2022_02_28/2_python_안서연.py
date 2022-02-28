import heapq # 최소힙

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while(scoville[0] < K):
        if len(scoville) <= 1:
            answer = -1
            break
        # min1 = scoville.pop(0)
        # min2 = scoville.pop(0)
        # new = min1 + (min2 *2)
        # scoville.append(new)
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, (min1 + (min2 * 2)))
        answer += 1

    return answer
