def solution(n):
    n_array = ['1', '2', '4']
    answer = ""

    # 3���� ���ڸ� ����ϱ� ������ 3�������� �����
    while n > 0:
        n -= 1
        answer = n_array[n%3] + answer
        n //=3
    return answer


# ������ �ڵ�, 10 �̻���ʹ� ���ϴ� ����� ������ ����.
# ���� 3�� ���� ���� �������� �ʾ��� 
def solution(n):
    answer = ''

    # n�� 3 ������ ��
    if n <=3:
        answer = '124'[n-1]

    # n�� 4 �̻��� ��
    else:
        if n % 3 == 1:
            answer = str(n//3) + str('1')
        elif n % 3 == 2:
            answer = str(n//3) + str('2')
        else:
            answer = str((n//3)-1) + str('4')
        
    return answer



