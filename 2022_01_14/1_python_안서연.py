def solution(n, lost, reserve):
    answer = n - len(lost)
    student = {}
    lost.sort()
    reserve.sort()
    
    for i in reserve:
        if(i in lost):
            lost.remove(i)
            answer += 1
            continue
        student[i] = []
        if(i-1 > 0):
            student[i].append(i-1)
        if(i+1 <= n):
            student[i].append(i+1)
    print(student)
    
    for ls_num in lost:
        for s_num, lendto in student.items():    
            if(ls_num in lendto):
                answer += 1
                del student[s_num]
                print(student)
                break
    
    return answer
