def solution(strings, n):
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()
    answer = [word[1:] for word in strings]
    return answer