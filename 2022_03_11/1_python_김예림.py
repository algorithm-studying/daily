from datetime import date
def solution(a, b):
    day=['MON','TUE','WED','THU','FRI','SAT','SUN']
    ans=date(2016,a,b)
    return day[ans.weekday()]
