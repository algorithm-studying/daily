def solution(s):
    result = []
    for s in s.split(' '):  
        new_str = ''
        for i in range(len(s)):  
            if i % 2 == 0:  
                new_str += s[i].upper() 
            else :
                new_str += s[i].lower()
        result.append(new_str) 
            
    return ' '.join(result)
