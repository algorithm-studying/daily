def solution(a, b):
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']  # 1월 1일은 금요일
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 2016년은 윤년
    cnt = 0
    
    for month in range(a):
        cnt += months[month]
    cnt += b
    day = cnt % 7
    
    return days[day]

'''
다른 사람 풀이:
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]


#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))
'''