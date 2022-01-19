def solution(s):
    answer = ''
    s_li = s.split(' ')
    
    for word in s_li:
        for i, w in enumerate(word):
            if i%2 == 0:
                answer += w.upper()
            else:
                answer += w.lower()
        answer += ' '
    
    answer = answer[:-1]
    return answer
