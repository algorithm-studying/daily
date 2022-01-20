def solution(d, budget):
    answer = 0
    d.sort()
    for company in d:
        budget -= company
        if budget < 0:
            break
        else:
            answer += 1
    return answer