
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reporter = {x: [] for x in id_list}
    for i in set(report):
        i = i.split()
        reporter[i[1]].append(i[0])

    for key, value in reporter.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1
    return answer
