def solution(n, lost, reserve):
    students = [1] * n
    
    for plus in reserve:
        students[plus-1] += 1
    
    for i in lost:
        students[i-1] -= 1
    
    reserve.sort()
    
    for serve in reserve:
        if students[serve-1] == 2:
            if serve >= 2 and students[serve-2] == 0:
                students[serve-1] = 1
                students[serve-2] = 1
            elif serve <  n and students[serve] == 0:
                students[serve-1] = 1
                students[serve] = 1
    
    answer = n - students.count(0)
        
    return answer