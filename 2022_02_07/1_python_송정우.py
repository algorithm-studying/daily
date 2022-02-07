def solution(arr):
    answer = []
    for i, v in enumerate(arr):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        answer.append(v)
    
    return answer