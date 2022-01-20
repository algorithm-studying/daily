def solution(d, budget):
    answer = 0
    summ = 0
    d.sort()
    for i in d:
        summ += i
        answer += 1
        if summ > budget:
            answer -= 1
            break
    return answer

'''
다른 사람 풀이:

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
'''