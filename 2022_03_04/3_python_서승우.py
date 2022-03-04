def solution(n):
    tiles = [1, 2]
    for i in range(2,n):
        tiles.append((tiles[i-1] + tiles[i-2])%1000000007)
    return tiles[n-1]