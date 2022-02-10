def solution(d, budget):
    d.sort()
    answer = 0
    for i in range(len(d)):
        if d[i] <= budget:
            budget -= d[i]
            answer += 1
        else: break
    return answer

# 별도로 지원 총금액을 합하는 변수를 따로 선언하지 말고
# 지원해준만큼의 금액을 그냥 예산에서 빼주면 됨!



