def solution(arr1, arr2):
    answer = []
    for i, v in enumerate(arr1):
        tmp = []
        for j, v2 in enumerate(v):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
    return answer
'''
다른 사람 풀이:
def sumMatrix(A,B):
    answer = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [3,4]], [[3,4],[5,6]]))
'''