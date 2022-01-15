# 레벨1_완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append('5')

    for i in range(0,len(participant)):
        if participant[i] != completion[i]:
            print(participant[i])
            break
    answer = participant[i]
    return answer


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))