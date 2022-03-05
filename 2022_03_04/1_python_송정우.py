def solution(n):
    answer = ''
    for i in range(1, n + 1):
        if i % 2 == 1:
            answer += "수"
        else:
            answer += "박"
    return answer

'''
다른 사람 풀이:
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)
'''