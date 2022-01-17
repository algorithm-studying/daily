def solution(x):
    add = 0
    x = str(x)
    for i in range(len(x)):
        add += int(x[i])

    if int(x) % add == 0:
        answer = True
    else:
        answer = False
    return answer