def solution(strings, n):
    answer = []
    for string in strings:
        answer.append(string[n]+string)
    answer.sort()
    answer = [a[1:] for a in answer]
    return answer