def solution(s):
    answer = ''
    tmp = s.split(' ')  # s에 공백을 포함한 문자가 들어오면 마지막에 그 공백도 출력해줘야 한다.
                        # s.split()으로 하면 모든 공백을 없애버리기 때문에 100점이 안나왔던 것.
                        # 출처: https://latte-is-horse.tistory.com/123
    for i in tmp:
        for j, v in enumerate(i):
            if j == 0 or j % 2 == 0:
                answer += v.upper()
                continue
            else:
                answer += v.lower() # 대문자로 입력받을 경우 필요
        answer += ' '
    return answer[:-1] # 맨 오른쪽 값을 제외하고 모두

'''
다른 사람 풀이:
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

# 람다식 공부하기
'''