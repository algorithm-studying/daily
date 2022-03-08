class Solution {
    public int[] solution(int brown, int yellow) {
        int[] rslt = new int[2];
        
        int sum = brown + yellow;
        int w, h;
        
        for(int i=2; i<sum; i++){
            if(sum%i==0){
                w = i;
                h = sum/i;
                
                if(w >= h){
                    if(w*2 + h*2 -4 == brown){
                        rslt[0] = w;
                        rslt[1] = h;
                    }
                }
            }
        }
        return rslt;
    }
}