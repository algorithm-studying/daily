def solution(sizes):
    a = [0]
    b = [0]
    
    i = 0
    while i <= 3:
        a.append(max(sizes[i][0],sizes[i][1]))
        b.append(min(sizes[i][0],sizes[i][1]))
        i = i + 1


    answer = max(a) * max(b)
    return answer


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))

sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(sizes))

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))