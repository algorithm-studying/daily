import math
def solution(left, right):
    result = 0
    for num in range(left, right+1):
        count = 2
        root = int(math.sqrt(num))
        
        for i in range(1, root+1): # 제곱근까지 구하고 x2하면 약수의 개수
            if num % i == 0:
                count += 2
            else:
                continue
                
        if root * root == num: # 제곱수인 경우 -1
            count -= 1
            
        if count % 2 == 0:
            result += num
        else:
            result -= num
    return result