def solution(numbers):
    temp_list = []
    while len(numbers) > 1:
        temp = numbers.pop()
        for i in range(len(numbers)):
            temp_list.append(temp + numbers[i])
    temp_set = set(temp_list)
    answer = list(temp_set)
    answer.sort()
    return answer