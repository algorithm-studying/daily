def solution(numbers, hand):
    answer = ''
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    lprev = keypad['*']
    rprev = keypad['#']
    
    for n in numbers:
        if(n in [1,4,7]):
            lprev = keypad[n]
            answer += 'L'
        elif(n in [3,6,9]):
            rprev = keypad[n]
            answer += 'R'
        else:
            ldist, rdist = 0, 0
            for l, r, this in zip(lprev,rprev,keypad[n]):
                ldist += abs(this-l)
                rdist += abs(this-r)
            if(ldist < rdist):
                lprev = keypad[n]
                answer += 'L'
            elif(ldist > rdist):
                rprev = keypad[n]
                answer += 'R'
            else:
                if(hand == 'left'):
                    lprev = keypad[n]
                    answer += 'L'
                else:
                    rprev = keypad[n]
                    answer += 'R'   
                
    return answer
