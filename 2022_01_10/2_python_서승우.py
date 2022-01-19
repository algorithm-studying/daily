def solution(n):
    a = ['0', '1', '2', '4']
    if n <= 3:
        return a[n]
    elif n % 3 == 0:
        return solution((n//3 - 1)) + a[3]
    else:
        return solution(n//3) + a[n%3]