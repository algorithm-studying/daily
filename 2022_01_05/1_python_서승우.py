def solution(array, commands):
    answer = []
    for i,j,k in commands:
        result = array[i-1:j]
        result.sort()
        answer.append(result[k-1])
    return answer