def solution(record):
    answer = []
    user_name = {}
    user_status = []
    user_id = []
    message = {'Enter': '들어왔습니다.', 'Leave': '나갔습니다.'}
    
    #log 분석
    for log in record:
        info = log.split(' ')
        if info[0] == 'Change':
            user_name[info[1]] = info[2]
            continue
        else:
            if info[0] == 'Enter':
                user_name[info[1]] = info[2]
            user_status.append(info[0])
            user_id.append(info[1])
            
    # 메세지 출력
    for status, uid in zip(user_status, user_id):
        answer.append(f'%s님이 %s' % (user_name[uid], message[status]))
        
    return answer