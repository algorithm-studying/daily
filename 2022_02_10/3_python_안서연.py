from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    cnt_li = [0]*n
    
    for a, b in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    q = deque()
    q.append(0)
    while q:
        node = q.popleft()
        visited[node] = True
        for num in graph[node]:
            if not visited[num]:
                visited[num] = True
                q.append(num)
                cnt_li[num] = cnt_li[node] + 1
    
    answer = cnt_li.count(max(cnt_li))
    return answer
