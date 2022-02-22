def solution(s):
    answer=[]
    en=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i,en in enumerate(en):
        if en in en:
            s=s.replace(en,str(i))
    return int(s)
