def solution(numbers, hand):
    answer = ''
    keypad = [[3,1], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
    left_location = [3,0]
    right_location = [3,2]

    for num in numbers:

        right_distance = abs((keypad[num][0] - right_location[0])) + abs((keypad[num][1] - right_location[1]))
        left_distance = abs((keypad[num][0] - left_location[0])) + abs((keypad[num][1] - left_location[1]))

        if num in [1,4,7]:
            left_location = keypad[num]
            answer += 'L'
            continue

        elif num in [3,6,9]:
            right_location = keypad[num]
            answer += 'R'
            continue

        elif left_distance == right_distance and hand == 'right':
            right_location = keypad[num]
            answer += 'R'
            continue

        elif left_distance == right_distance and hand == 'left':
            left_location = keypad[num]
            answer += 'L'
            continue

        elif left_distance > right_distance:
            right_location = keypad[num]
            answer += 'R'
            
        else:
            left_location = keypad[num]
            answer += 'L'
    return answer