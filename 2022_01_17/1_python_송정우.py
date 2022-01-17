def solution(x):
    answer = False
    sum_n = 0
    
    for i in str(x):
        sum_n += int(i)
    
    if x % sum_n == 0:
        answer = True
        
    return answer

'''
다른 사람 코드:
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))
'''