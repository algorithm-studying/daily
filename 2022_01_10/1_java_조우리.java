class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int cnt = 0;
        int zero = 0;
        int[] rslt = new int[2];
        
        for(int i=0; i<lottos.length; i++){
            for(int j=0; j<win_nums.length; j++){
                if(win_nums[j] == lottos[i])
                    cnt++;
            }
            if(lottos[i] == 0)  zero++;
        }
        if(zero == 0){
            if(cnt != 0){
                rslt[0] = 7-cnt;
                rslt[1] = 7-cnt;
            }
            else{
                rslt[0] = 6;
                rslt[1] = 6;
            }
        }
        else if(zero != 6){
            rslt[0] = 7-(cnt+zero);
            rslt[1] = 7-cnt;
        }
        else{
            rslt[0] = 1;
            rslt[1] = 6;
        }
        return rslt;
    }
}