def solution(record):
    answer = []
    user = {}
    string = []
    
    for r in record:
        check = r.split()
        
        if check[0] == 'Enter':
            if check[1] in user:
                user[check[1]] = check[2]
                string.append([check[1],'님이 들어왔습니다.'])
            else:
                user[check[1]] = check[2]
                string.append([check[1],'님이 들어왔습니다.'])
                
        elif check[0] == 'Leave':
            string.append([check[1],'님이 나갔습니다.'])
            
        elif check[0] == 'Change':
            user[check[1]] = check[2]
    
    answer = [user[s[0]]+s[1] for s in string]        
    return answer
