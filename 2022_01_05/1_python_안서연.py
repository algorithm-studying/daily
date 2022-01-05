def solution(array, commands):
    answer = []
    
    for c in commands:
        slice_array = array[(c[0]-1):c[1]]
        slice_array.sort()
        answer.append(slice_array[(c[2]-1)])
    
    return answer
