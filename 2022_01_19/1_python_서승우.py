def solution(s):
    answer = ''
    a = list(s)
    index = 2
    for i in a:
        if i == ' ':
            answer += i
            index = 2
            continue
        elif index % 2 == 0:
            answer += i.upper()
            index += 1
        else:
            answer += i.lower()
            index += 1
    return answer