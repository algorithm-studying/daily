# 레벨1_하샤드_수

import copy
def solution(x):
    sum=0
    k = copy.deepcopy(x)
    for i in range(1,len(str(k))):
        sum += (x//(10**(len(str(k))-i)))
        x = x%(10**(len(str(k))-i))
    sum += x
    if int(k%sum) == 0:
        answer = True
    elif int(k%sum) != 0:
        answer = False
    return answer

