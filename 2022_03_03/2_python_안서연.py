def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for n in range(3,total//2):
        if total%n == 0:
            quota = total//n
            li = [n,quota]
            if (n-2)*2+quota*2 == brown:
                answer = li
                break
    answer.sort(reverse=True)
    return answer
