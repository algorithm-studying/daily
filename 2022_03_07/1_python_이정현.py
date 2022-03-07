def solution(a, b):
    answer = 0
    if a<b:
        answer = (b*(b+1) - a*(a-1)) / 2
        return int(answer)
    elif a>b:
        answer = (a*(a+1) - b*(b-1)) / 2
        return int(answer)
    else:
        return a


print(solution(3,5))