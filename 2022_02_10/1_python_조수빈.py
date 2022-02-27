# 레벨1_나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    for arr1 in arr:
        if arr1%divisor==0:
            answer.append(arr1)
    if len(answer)==0:
        answer.append(-1)
    answer.sort(reverse=False)
    return answer


