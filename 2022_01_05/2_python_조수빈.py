# 레벨2_최솟값 만들기
'''1. A는 오름차순, B는 내림차순으로 정렬
   2. 각각의 자릿수 값을 곱하기
   3. 더해서 누적'''


def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    c = [a * b for a, b in zip(A, B)]
    answer = sum(c)

    return answer