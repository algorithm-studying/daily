def solution(n, times):
    answer = 0
    l, r = 1, max(times) * n
    
    while(l <= r):
        mid = (l+r)//2
        people = 0
        for t in times:
            people += mid // t
            if people >= n:
                break
        
        if people >= n:
            r = mid - 1
            answer = mid
        else:
            l = mid + 1
    
    return answer
