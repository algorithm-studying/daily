array = [1,5,2,6,3,7,4]
commands = [[2,5,3], [4,4,1], [1,7,3]]


def solution(array, commands):
    answer = []
    for command in commands:
        array1 = array[command[0]-1:command[1]]
        array1.sort()
        answer.append(array1[command[2]-1])
    return answer


