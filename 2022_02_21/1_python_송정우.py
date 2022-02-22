en_num = {"zero" : "0", "one": "1", "two": "2", "three": "3", "four": "4",
             "five": "5", "six": "6", "seven": "7", "eight": "8",
             "nine": "9", "ten": "10"}

def solution(s):
    for i, en in enumerate(en_num):
        if en in s:
            s = s.replace(en, en_num[en])
    return int(s)

'''
다른 사람 풀이:
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
'''