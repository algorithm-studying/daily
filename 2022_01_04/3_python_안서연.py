def solution(m, n, puddles):
    answer = 0
    
    mtx = [[0]*(m+1) for i in range(n+1)]
    mtx[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            elif [j,i] in puddles:
                mtx[i][j] = 0
            else:
                mtx[i][j] = mtx[i-1][j] + mtx[i][j-1]
    
    answer = mtx[n][m]%1000000007
    return answer
