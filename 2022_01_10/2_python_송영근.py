def solution(n):
    a=[]
    i=1
    while n!=0:
        if (n-1)%3==0:
            a.append(1)
        elif (n-1)%3==1:
            a.append(2)
        else:
            a.append(4)
        n = (n-1)//3 
        i+=1
    answer = ''
    a.reverse()
    for j in a:
        answer+=str(j)
    return answer