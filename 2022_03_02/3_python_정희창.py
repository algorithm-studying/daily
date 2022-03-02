def solution(n, works):
    if n >= sum(works):
        return 0
    while n > 0 :
        works[works.index(max(works))] -=1
        n -= 1
        
    return sum([i ** 2 for i in works])
