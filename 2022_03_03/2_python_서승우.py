def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0: # 노란 타일의 배열 (1줄, 2줄 ...)
            up_down = int((yellow / i) * 2 + 4) # 위 아래 brown 타일 수
            sides = int(i * 2) # 좌우 brown 타일 수
            if (up_down + sides) == brown:
                return [up_down/2, i+2]