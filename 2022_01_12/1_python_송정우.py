def solution(participant, completion):
    answer =''
    participant.sort()
    completion.sort()
    for i in range(len(participant) - 1):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        else:
            answer = participant[-1]
    
    return answer

'''
다른 사람 풀이

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

'''
# collentions.Counter()는 딕셔너리 형태로 리턴한다.
'''
ex) lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
print(collections.Counter(lst))

결과
Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})

출처: https://excelsior-cjh.tistory.com/94 [EXCELSIOR]
'''