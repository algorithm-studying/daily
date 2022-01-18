def solution(arr1, arr2):
    answer = []
    
    for i1 in range(len(arr1)):
        res = []
        for i2 in range(len(arr1[i1])):
            res.append(arr1[i1][i2] + arr2[i1][i2])
        answer.append(res)
    
    return answer
