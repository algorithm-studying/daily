def solution(s):
    answer = []
    set_li = [ss for ss in s.split('},{')]
    for i in range(len(set_li)):
        new = set_li[i].replace('{', '')
        new = new.replace('}', '')
        new = list(map(int, new.split(',')))
        set_li[i] = new
    
    set_li.sort(key=lambda x:len(x))
    
    for s in set_li:
        for ss in s:
            if ss not in answer:
                answer.append(ss)
                break

    return answer
