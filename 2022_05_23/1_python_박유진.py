def solution(n):
    three = []
    answer = 0
    # while n > 3으로 해버리면, n = 3일 때 틀림
    while n > 0 :
        three.append(n % 3)
        n //= 3
    for i in range(len(three)):
        answer += three[i] * (3**(len(three)-1-i))
        print(answer)
    return answer

def solution(n):
    answer = ''
    while n > 0:
        n, rem = divmod(n, 3)
        answer += str(rem)
    return int(answer, 3)