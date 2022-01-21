def solution(n):
    n_bn=bin(n)
    cnt=n_bn.count('1')
    answer=0
    for i in range(n+1,1000001):
        bn=bin(i)
        if bn.count('1')==cnt:
            return int(bn,2)
