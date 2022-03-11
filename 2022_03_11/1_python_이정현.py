def solution(a, b):
    weeks = {3:'SUN', 4:'MON', 5:'TUE', 6:'WED', 0:'THU', 1:'FRI', 2:'SAT'}
    cnt = 0
    while a > 1:
        a -= 1
        if a in [1,3,5,7,8,10,12]:
            cnt += 31
        elif a == 2:
            cnt += 29
        else:
            cnt += 30
    cnt += b
    return weeks[cnt%7]