def solution(n):
    answer = ''
    num = ['4','1','2']
          
    while n > 0:
        if n % 3 == 0:
            answer = '4' + answer
            n = int(n / 3) - 1
        else:
            n, mod = divmod(n, 3)
            answer = num[mod] + answer
        
    return answer
