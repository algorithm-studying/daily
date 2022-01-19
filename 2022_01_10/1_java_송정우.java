class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int cnt = 0, possibility = 0, tot_cnt = 0;
        
        for(int win_num: win_nums) {
            for(int i = 0; i < 6; i++) {
                if(lottos[i] == win_num) {
                    cnt++;
                    break;
                }
            }
        }
        
        for(int j = 0; j < 6; j++) {
            if(lottos[j] == 0)
                possibility++;
        }
        
        tot_cnt = cnt + possibility;
        
        if(tot_cnt >= 6)
            answer[0] = 1;
        else if(tot_cnt == 5)
            answer[0] = 2;
        else if(tot_cnt == 4)
            answer[0] = 3;
        else if(tot_cnt == 3)
            answer[0] = 4;
        else if(tot_cnt == 2)
            answer[0] = 5;
        else
            answer[0] = 6;
        
        if(cnt == 6)
            answer[1] = 1;
        else if(cnt == 5)
            answer[1] = 2;
        else if(cnt == 4)
            answer[1] = 3;
        else if(cnt == 3)
            answer[1] = 4;
        else if(cnt == 2)
            answer[1] = 5;
        else
            answer[1] = 6;
        
        return answer;
    }
}

/* 다른 사람 코드
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int zero = 0;
        int matched = 0;
        for (int l : lottos) {
            if (l == 0) {
                zero++;
            } else {
                for (int w : win_nums) {
                    if (l == w) {
                        matched++;
                        break;
                    }
                }
            }
        }
        int min = matched;
        int max = matched + zero;
        int[] answer = {Math.min(7 - max, 6), Math.min(7 - min, 6)};
        return answer;
    }
}
*/