def solution(a, b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']

    return  day[(sum(month[:a-1]) + b-1)%7]
