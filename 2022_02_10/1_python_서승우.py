def solution(arr, divisor):
    answer = []
    flag = False
    arr.sort()
    for num in arr:
        if num % divisor == 0:
            flag = True
            answer.append(num)
    return [-1] if flag == False else answer