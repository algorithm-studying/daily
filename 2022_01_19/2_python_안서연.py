def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for pb in range(len(phone_book)-1):
        pb1 = phone_book[pb]
        pb2 = phone_book[pb+1]
        if(pb1 == pb2[:len(pb1)]):
            answer = False
            break
    
    return answer
