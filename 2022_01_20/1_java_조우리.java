import java.util.Arrays;

class Solution {
    public int solution(int[] d, int budget) {
        int rslt = 0;
        
        Arrays.sort(d);
        
        for(int i=0; i<d.length; i++){
            if(budget >= d[i]){
                rslt++;
                budget -= d[i];
            }
        }
        
        return rslt;
    }
}