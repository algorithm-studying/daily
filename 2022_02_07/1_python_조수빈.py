# 레벨1_같은 숫자는 싫어

def solution(arr):
    answer = []
    last_num=arr[0]
    answer.append(arr[0])
    for num in arr:
        if num != last_num:
            answer.append(num)
        last_num = num
    return answer


arr = [1,1,3,3,0,1,1]
print(solution(arr))
arr=[4,4,4,3,3]
print(solution(arr))