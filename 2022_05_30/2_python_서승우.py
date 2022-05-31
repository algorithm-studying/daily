def solution(n):
    ans = 0
    while True:
        if n == 0:
            break
        elif n % 2 != 0:
            n -= 1
            ans += 1
        else:
            n /= 2
    return ans

'''
같은 논리, 더 간결한 풀이
return bin(n).count('1')
'''