def solution(numbers):
    answer = []
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer


def solution(numbers):
    answer = []
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    # answer.sort()
    # set(answer)
    # 이런 식으로 하니까 제대로 안 나옴
    # 이렇게 해야 함
    return sorted(list(set(answer)))