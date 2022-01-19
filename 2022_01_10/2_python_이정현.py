def solution(n):

    list = []
    temp = 0
    exp_three = 3
    cnt = 0

# 3의 지수만큼 반복해서 빼기
    while(n > 0):
        temp = n
        n -= exp_three
        exp_three *= 3
        cnt += 1

    n = temp -1

# 3진법으로 계산. 그리고 각각을 0->1, 1->2, 2->4 로 변환
    for i in range(0,cnt):
        if n%3 == 0:
            temp = 1
        elif n%3 == 1:
            temp = 2
        else:
            temp = 4
        list.insert(0, temp)
        n //= 3


# 정수형 리스트를 문자로 합쳐서 반환
    answer = ''.join([str(_) for _ in list])  
    return answer


n = 38 # 442
print(solution(n))
