def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                flag=0
                for n in range(2, (nums[i]+nums[j]+nums[k])):
                    if (nums[i]+nums[j]+nums[k])%n==0:
                        flag=1
                if flag==0:
                    answer+=1


    return answer