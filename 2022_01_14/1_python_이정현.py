def solution(n, lost, reserve):
    list1 = []

    for i in range(n):
        list1.append(1)
    
    list1.insert(0,-1)

    for j in lost:
        list1[j] -= 1

    for k in reserve:
        list1[k] += 1

    for l in range(1,n):
        if list1[l] == 0:
            if list1[l+1] == 2:
                list1[l] += 1
                list1[l+1] -= 1
    
    for m in range(1,n):
        if list1[m] == 2:
            if list1[m+1] == 0:
                list1[m] -= 1
                list1[m] += 1
    

    answer = list1.count(1) + list1.count(2)

    return answer


n = 5
lost =[2,4]
reserve = [1,3,5]
print(solution(n,lost,reserve))

n = 5
lost = [2,4]
reserve = [3]
print(solution(n,lost,reserve))

n = 3
lost = [3]
reserve = [1]
print(solution(n,lost,reserve))