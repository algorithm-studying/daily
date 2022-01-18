def solution(arr1, arr2):
    answer = arr1
    for i,list_a in enumerate(arr2):
        for j, num in enumerate(list_a):
            answer[i][j] += num
    return answer