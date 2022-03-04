import heapq # 최대힙(값을 음수로 변환)
def solution(n, works):
    answer = 0
    works = [-w for w in works]
    works.sort() # sort 필수
    
    for _ in range(n):
        num = heapq.heappop(works)
        if num == 0:
            break
        heapq.heappush(works, num+1)

    for num in works:
        answer += num*num
    return answer
