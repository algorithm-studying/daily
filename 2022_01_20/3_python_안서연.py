########## DFS 재귀 이용 ##########
def DFS(i, n, computers, node):
    node[i] = True
    for j in range(n):
        if computers[i][j] and not node[j]:
            DFS(j, n, computers, node)

def solution(n, computers):
    answer = 0
    node = [False for i in range(n)]
    
    for i in range(n):
        if node[i] == False:
            DFS(i, n, computers, node)
            answer += 1
    
    return answer


########## BFS 스택 이용 ##########
from collections import deque
def BFS(i, n, computers, node):
    q = deque()
    q.append(i)
    while q:
        j = q.popleft()
        node[j] = True
        for k in range(n):
            if computers[j][k] and not node[k]:
                q.append(k)
    
def solution(n, computers):
    answer = 0
    node = [False for i in range(n)]
    
    for i in range(n):
        if node[i] == False:
            BFS(i, n, computers, node)
            answer += 1
    
    return answer
