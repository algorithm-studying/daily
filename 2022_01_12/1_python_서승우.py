def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        elif i == len(completion)-1:
            answer = participant[i+1]
    return answer