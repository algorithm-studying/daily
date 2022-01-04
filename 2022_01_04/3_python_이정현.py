import operator as op
from functools import reduce

def nCr(n, r):
    if n<1 or r<0 or n<r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

def solution(m, n, puddles):
    a = puddles[0][0] 
    b = puddles[0][1]
    answer = nCr(m+n-2,m-1) - (nCr(a+b-2,a-1) * nCr((m-a)+(n-b),m-a))
    return answer

print(solution(4, 3, [[2,2]]))