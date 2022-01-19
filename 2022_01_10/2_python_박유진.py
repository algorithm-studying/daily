def solution(n):
    n_array = ['1', '2', '4']
    answer = ""

    # 3개의 숫자를 사용하기 때문에 3진법으로 만들기
    while n > 0:
        n -= 1
        answer = n_array[n%3] + answer
        n //=3
    return answer


# 실패한 코드, 10 이상부터는 원하는 결과가 나오지 않음.
# 몫이 3이 나올 때를 생각하지 않았음 
def solution(n):
    answer = ''

    # n이 3 이하일 때
    if n <=3:
        answer = '124'[n-1]

    # n이 4 이상일 때
    else:
        if n % 3 == 1:
            answer = str(n//3) + str('1')
        elif n % 3 == 2:
            answer = str(n//3) + str('2')
        else:
            answer = str((n//3)-1) + str('4')
        
    return answer



