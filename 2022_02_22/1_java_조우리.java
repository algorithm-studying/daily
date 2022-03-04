class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int rslt = 0;
        for(int i=0; i<absolutes.length; i++){
            if(signs[i] == true){
                rslt += absolutes[i] * 1;
            }else{
                rslt += absolutes[i] * (-1);
            }
        }
        
        return rslt;
    }
}