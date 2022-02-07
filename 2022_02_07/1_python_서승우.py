def solution(arr): 
    cursor = -1
    answer = []
    for num in arr:
        if cursor != num:
            answer.append(num)
            cursor = num
    return answer