
def solution(lottos, win_nums):
    answer=[]
    unknown=0 #알아볼 수 없는 값
    for i in lottos:
        if i==0:
            unknown+=1
    win_num=set(lottos)&set(win_nums) #같은 값 찾기
    max=unknown+len(win_num) #최대 일치 번호 갯수
    min=len(win_num) #최소 일치 번호 갯수
    
    if (max>=2):
        answer.append(7-max)
    else:
        answer.append(6)
    if(min >=2):
        answer.append(7-min)
    else:
        answer.append(6)
        
    return answer