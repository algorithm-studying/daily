def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0,0,0]
    answer = []
    for i in range(0,len(answers)):
        if answers[i] == student1[i%5]:
            cnt[0]+=1
        if answers[i] == student2[i%8]:
            cnt[1]+=1
        if answers[i] == student3[i%10]:
            cnt[2]+=1
    
    for i in range(3):
        if cnt[i] == max(cnt):
            answer.append(i+1)
        
    return answer
