def solution(s):
    answer = 1
    N = len(s)
    for i in range(2, N+1):
        for j in range(N-i+1):
            word = s[j:j+i]
            if word == word[::-1]:
                answer = i
    return answer