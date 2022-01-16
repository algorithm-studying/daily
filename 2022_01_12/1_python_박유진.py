def solution(participant, completion):
    n = len(completion)

    participant.sort()
    completion.sort()

    for i in range(n):
        if participant[i] != completion[i] :
            return participant[i]
            
    # for를 다 돌았을 때에 participant의 마지막 사람이 completion에 없는 경우
    return participant[-1]

p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]
p = ["marina", "josipa", "nikola", "vinko", "filipa"]
c = ["josipa", "filipa", "marina", "nikola"]
solution(p,c)


# 다른 리스트에 카피해서 있으면 제거하기
# 정답은 나오지만, 시간 초과 코드
def solution(participant, completion):
    participant1 = participant.copy()
    n = len(participant)

    for i in range(n):
        if completion[i] in participant:
            participant1.remove(completion[i])

    return participant1[0]


# 해시 함수로 시도
def solution(participant, completion):
    part_dic = {}
    comp_dic = {}
    answer = []

    #리스트에 hash function(모듈로 연산)으로 키 값 정하고
    #part_dic 딕셔너리에 저장하기
    for name in participant:
        key = 0
        for letter in name: 
            key += ord(letter)
        key %= 100
        part_dic[key] = name

    print(part_dic)

    # completion에 있는 것들도 키 값 정하고 
    # comp_dic 딕셔너리에 저장하기
    for name in completion:
        key = 0
        for letter in name: 
            key += ord(letter)
        key %= 100
        comp_dic[key] = name



# 다른 사람 코드: 간단하게 이름 자체를 key로, 그리고 사람의 
# 수를 value로 두었음. 
def solution(participant, completion):
    dic = {}

    for i in range(len(participant)):
        dic[participant[i]] = 0

    for i in participant:
        dic[i] += 1
    
    for i in completion:
        dic[i] -= 1

    # 중복된 사람이 있을 때 그 사람 리턴하기
    for i in dic:
        if dic[i] > 0:
            return i
    
    return -1




