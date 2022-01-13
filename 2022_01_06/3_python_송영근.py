# 정확성: 16.5
# 효율성: 15.3
# 합계: 31.8 / 100.0

def solution(s):
    count=[]
    for i in range(1, len(s)//2+1 if len(s)%2==1 else len(s)//2 ):
        a=0
        for j in range(1,i+1):
            if s[i-j]==s[i+j]:
                a+=1
        count.append(a*2+1)

    for i in range(-2, (len(s)//2+1)*(-1) if len(s)%2==1 else (len(s)//2+1)*(-1), -1):
        a=0
        for j in range(1,-i):
            if s[i-j]==s[i+j]:
                a+=1
        count.append(a*2+1)
    

    return max(count)