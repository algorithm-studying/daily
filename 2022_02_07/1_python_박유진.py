def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

#항상 헷갈리는 list index 문제 i-1이 있다는 것도 명심하자!