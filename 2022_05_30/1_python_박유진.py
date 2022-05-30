def solution(strings, n):
    temp = []
    answer = []
    for string in strings:
        temp.append(string[n]+string) # 먼저 n 번째 글자 기준으로 정렬하기 위해 앞에 그 n번째 글자 붙여 버리기!
    temp.sort()
    for t in temp:
        answer.append(t[1:])
    return answer

# 또 다른 멋진 풀이
def strange_sort(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)
    return strings