def solution(participant, completion):
    n = len(completion)

    participant.sort()
    completion.sort()

    for i in range(n):
        if participant[i] != completion[i] :
            return participant[i]
            
    # for�� �� ������ ���� participant�� ������ ����� completion�� ���� ���
    return participant[-1]

p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]
p = ["marina", "josipa", "nikola", "vinko", "filipa"]
c = ["josipa", "filipa", "marina", "nikola"]
solution(p,c)


# �ٸ� ����Ʈ�� ī���ؼ� ������ �����ϱ�
# ������ ��������, �ð� �ʰ� �ڵ�
def solution(participant, completion):
    participant1 = participant.copy()
    n = len(participant)

    for i in range(n):
        if completion[i] in participant:
            participant1.remove(completion[i])

    return participant1[0]


# �ؽ� �Լ��� �õ�
def solution(participant, completion):
    part_dic = {}
    comp_dic = {}
    answer = []

    #����Ʈ�� hash function(���� ����)���� Ű �� ���ϰ�
    #part_dic ��ųʸ��� �����ϱ�
    for name in participant:
        key = 0
        for letter in name: 
            key += ord(letter)
        key %= 100
        part_dic[key] = name

    print(part_dic)

    # completion�� �ִ� �͵鵵 Ű �� ���ϰ� 
    # comp_dic ��ųʸ��� �����ϱ�
    for name in completion:
        key = 0
        for letter in name: 
            key += ord(letter)
        key %= 100
        comp_dic[key] = name



# �ٸ� ��� �ڵ�: �����ϰ� �̸� ��ü�� key��, �׸��� ����� 
# ���� value�� �ξ���. 
def solution(participant, completion):
    dic = {}

    for i in range(len(participant)):
        dic[participant[i]] = 0

    for i in participant:
        dic[i] += 1
    
    for i in completion:
        dic[i] -= 1

    # �ߺ��� ����� ���� �� �� ��� �����ϱ�
    for i in dic:
        if dic[i] > 0:
            return i
    
    return -1




