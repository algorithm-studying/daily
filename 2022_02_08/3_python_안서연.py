def solution(triangle):
    answer = 0
    matrix = [[-1] * len(triangle) for _ in range(len(triangle))]
    
    for i, num_li in enumerate(triangle):
        j = 0
        for inum in range(i,-1,-1):
            matrix[inum][j] = num_li[j]
            j += 1
    
    for i in range(len(matrix)):
        j = 0
        for inum in range(i,-1,-1):
            if((i,j) == (0,0)):
                    continue
            if(matrix[inum][j] >= 0):
                matrix[inum][j] = max(matrix[inum][j]+matrix[inum-1][j], matrix[inum][j]+matrix[inum][j-1])
                j += 1
    
    answer = max([max(m) for m in matrix])
    return answer
