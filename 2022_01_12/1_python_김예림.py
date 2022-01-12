def solution(participant, completion):
    participant.sort()
    completion.sort() 
    answer=participant[-1]
    for p, c in zip(participant, completion):
        if p!=c:
            answer=p
            break
    return answer

