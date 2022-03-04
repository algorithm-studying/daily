def nCr(n,r):
    from math import factorial
    return factorial(n) / (factorial(n-r) * factorial(r))

def solution(n):
    answer = 0
    for duo in range(n//2 + 1):
        solo = n - 2 * duo
        answer += nCr((solo + duo), duo)

    return int(answer)