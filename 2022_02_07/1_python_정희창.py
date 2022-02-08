def solution(arr):
    answer = []
    comp = -1

    for i in arr:
        if comp != i:
            answer.append(i)
            comp = i
            
    return answer
