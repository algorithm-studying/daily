def solution(s):
    try:
        int(s)
        return True if len(s) in [4,6] else False
    except:
        return False