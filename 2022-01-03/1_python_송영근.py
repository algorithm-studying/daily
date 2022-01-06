def solution(numbers):
    j=0
    
    for i in range(10):
        if numbers.count(i)== 0 :
            j+=i
            
    answer = j
    return answer