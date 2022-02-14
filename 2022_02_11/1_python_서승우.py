def solution(s):
    length = int(len(s) / 2)
    if len(s) % 2 == 0:
        answer = s[length-1] + s[length]
    else:
        answer = s[length]
    return answer