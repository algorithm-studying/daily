def solution(w,h):
    answer = 0
    
    # 최대 공약수 구하기
    if w > h:
        maximum = w
    else:
        maximum = h

    for i in range(maximum, 0, -1):
        if w % i == 0 and h % i == 0:
            gcd = i
            break


    # 멀쩡한 사각형의 개수는 전체 개수 - (w + h - 최대공약수)
    answer = w * h - (w + h - gcd)
        
    return answer


    #최대 공약수 구하기 2(유클리드 호제법)

def Euclidean(x, y):
    if x == 0: return y
    else:
        return (x%y, y)