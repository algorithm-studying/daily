def solution(s):
    answer = []
    temp = ''
    s = s.split(" ")
    
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j % 2 :
                temp += s[i][j].lower()
            else:
                temp += s[i][j].upper()
        answer.append(temp)
        temp = ''
    #리스트 문자열로 이어붙이기(공백 살리기)
    return (" ").join(answer)