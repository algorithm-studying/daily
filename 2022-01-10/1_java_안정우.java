class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] rank = {6,6,5,4,3,2,1};
        int zero = 0, cnt = 0;

        for (int i : lottos) {
            if (i == 0) {
                zero++;
                continue;
            }
            for (int j : win_nums)
                if (j == i) {
                    cnt++;
                    break;
                } 
        }
        int[] answer = {rank[cnt+zero],rank[cnt]};
        return answer;
    }
}
