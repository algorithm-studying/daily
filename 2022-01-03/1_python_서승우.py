# 없는 수를 찾아 더하는 풀이
# def solution(numbers):
#     answer = 0
#     full_num = [0,1,2,3,4,5,6,7,8,9]
#     for i in full_num:
#         if i not in numbers:
#             answer += i
#     return answer

# 없는 수의 합 = 0부터 9까지의 총 합 - 현재 있는 숫자의 합
def solution(numbers):
    return 45 - sum(numbers)