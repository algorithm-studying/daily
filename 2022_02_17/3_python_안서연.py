def solution(genres, plays):
    answer = []
    musics = {g:[] for g in set(genres)}
    sum_plays = {g:0 for g in set(genres)}
    
    for i, genre in enumerate(genres):
        musics[genre].append([plays[i],i])
        sum_plays[genre] += plays[i]

    sorted_sum_plays = sorted(sum_plays.items(), key=lambda x: -x[1])
    for genre, _ in sorted_sum_plays:
        li = sorted(musics[genre], key=lambda x:(-x[0],x[1]))[:2]
        answer += [l[1] for l in li]
            
    return answer
