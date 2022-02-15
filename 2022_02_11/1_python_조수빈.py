# 레벨1_가운데 글자 가져오기

def solution(s):
    answer = ''
    s_list=list(s)
    half=len(s)/2
    if len(s)%2==0:
        answer+=(s_list[int(half-1)])
        answer+=(s_list[int(half)])
    else:
        answer+=(s_list[int(half)])
    return answer