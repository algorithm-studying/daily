import heapq

def solution(n, works):
    answer = 0
    if n > sum(works):
        return answer

    # heap[0]이 최소이므로 -1 곱해주고 힙 만들기
    works = [-work for work in works]
    heapq.heapify(works)

    for _ in range(n):
        # 최솟값 반환
        work = heapq.heappop(works)
        work += 1
        # 힙 유지하면서 다시 넣어주기
        heapq.heappush(works, work)
        
    for work in works:
        answer += work * work
    return answer