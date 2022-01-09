import math

def solution(nums):
    answer = 0

    for i in range(0, len(nums)-2, 1):
        for j in range(i+1, len(nums)-1, 1):
            for k in range(j+1, len(nums), 1):
                add= nums[i] + nums[j] + nums[k]
                

                is_prime = True
                for x in range(2, int(math.sqrt(add))+1):
                    if add % x == 0:
                        is_prime = False
                        break

                if is_prime == True:
                    answer += 1

    return answer



