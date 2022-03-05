def solution(brown, yellow):
    a = 2
    b = 4 - brown
    c = 2 * yellow

    n = (-b - (b**2-4*a*c)**0.5)/(2*a)
    m = brown/2 - 2 - n

    answer = [int(m+2),int(n+2)]
    return answer