# 레벨1_모의고사

def solution(answers):
    answer = []
    student1 = [1, 2, 3, 4, 5]
    student2= [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1, s2, s3 = 0, 0, 0
    for num in range(len(answers)):
        if student1[num%len(student1)]==answers[num]:
            s1+=1
        if student2[num % len(student2)] == answers[num]:
            s2 += 1
        if student3[num % len(student3)] == answers[num]:
            s3 += 1
    max_num=max(s1, s2, s3)
    if max_num==s1:
        answer.append(1)
    if max_num==s2:
        answer.append(2)
    if max_num == s3:
        answer.append(3)
    answer.sort(reverse=False)
    return answer
