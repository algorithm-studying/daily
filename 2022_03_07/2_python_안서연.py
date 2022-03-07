def solution(s):
    answer = 0
    li = []
    
    if len(s) == 1: # 예외1 : 길이 1인 경우
        li.append(1)
    
    for i in range(len(s)//2, 0, -1):
        a, b = 0, i
        length = 0
        pattern = s[a:b]
        cnt = 1
        while(b<=len(s)):
            a += i
            b += i
            if pattern == s[a:b]:
                cnt += 1
                print(cnt)
            else:
                if cnt >= 10: # 예외2 : 10 이상으로 글자수+1이 아닌 글자수+2일 경우
                    length += i + 2
                elif cnt > 1:
                    length += i + 1
                else:
                    length += i
                pattern = s[a:b]
                cnt = 1
        length += len(s)%i
        li.append(length)
    
    answer = min(li)
    return answer
