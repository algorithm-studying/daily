def solution(id_list, report, k):
    dict_repo = {id:set() for id in id_list}
    dict_mails = {id:0 for id in id_list}
    ban_li = []
    
    for r in report:
        a,b = r.split()
        dict_repo[b].add(a)
    
    for ban_id, mail_ids in dict_repo.items():
        if len(mail_ids) >= k:
            for m_id in mail_ids:
                dict_mails[m_id] += 1
    
    answer = list(dict_mails.values())
    return answer
