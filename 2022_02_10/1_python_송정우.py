def solution(arr, divisor):
    arr.sort()
    answer = [arr[i] for i in range(len(arr)) if arr[i] % divisor == 0]
    if len(answer) == 0:
        answer.append(-1)
    return answer
'''
다른 사람 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
'''