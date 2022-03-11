# 레벨1_2016년

def solution(a, b):
    answer = ''
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    if a != 1:
        for month in range(1,a):
            if month == 1 or month == 3 or month == 5 \
                    or month == 7 or month == 8 \
                    or month == 10 or month == 12:
                b += 31
            elif month == 2 :
                b += 29
            else:
                b += 30
    answer = day[b % 7]
    return answer

(a, b)= (1, 1)
print(solution(a, b))
(a, b)= (5, 24)
print(solution(a, b))
