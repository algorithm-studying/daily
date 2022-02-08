def solution(s):
    try:
        int(s)
        if len(s) in [4,6]:
            return True
        return False
    except:
        return False
      
def solition(s):
    #함수를 완성하세요

    return s.isdigit() and (len(s) == 4 or len(s) == 6)

#isdigit : 문자열이 '숫자'로만 이루어져있는지 확인하는 함수 입니다.

#isnumeric : 전체 식이 숫자로 인식되는 경우 IsNumeric은True를 반환합니다. 그렇지 않으면 False 를 반환합니다.

#isdemical :  int로 바로 변환할 수 있는 수인지를 검사한다.
