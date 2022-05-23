def solution(n):
    answer =0
    t = ''
    while(n >= 1):
        rest = n % 3
        n = n // 3
        t += str(rest)

    for i in range(len(t)):
        a = 3**(len(t)-i-1)
        answer += int(t[i])*a

    return answer

# n진법으로 나타낸 수 다시 숫자로 되돌릴 수 있는 int('1200', 3) -> 45 
# int()는 디폴트로 10을 포함
