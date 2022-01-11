# def check(s, pals):
#     pal = 1
#     if len(s) == 0:
#         pals.append(0)
#         return
#     if len(s) <= 2:
#         pals.append(pal)
#         return
    
#     for idx in range(1,len(s)-1):
#         i = 1
#         while(True):
#             if(s[idx-i] == s[idx+i]):
#                 pal += 2
#                 i += 1
#                 if((idx-i) < 0 or (idx+i) >= len(s)):
#                     pals.append(pal)
#                     pal = 1
#                     break
#             else:
#                 pals.append(pal)
#                 pal = 1
#                 break
#     return

def check(x):
    if(x == x[::-1]):
        return True
    
def solution(s):
    answer = 0
#     pals = []
#     check(s, pals)
#     answer = max(pals)

    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if(check(s[i:j])):
                if(answer < len(s[i:j])):
                    answer = len(s[i:j])
                    
    return answer
