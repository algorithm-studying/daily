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
