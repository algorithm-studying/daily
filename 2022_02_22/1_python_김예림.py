def solution(absolutes, signs):
    result=0
    for i,signs in enumerate(signs):
        if signs==False:
            result-=absolutes[i]
        else:
            result+=absolutes[i]
    return result
