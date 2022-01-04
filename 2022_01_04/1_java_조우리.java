class Solution {
    public int solution(int[][] sizes) {

        int rslt;
        
        for(int i=0; i<sizes.length; i++){
            for(int j=0; j<2; j++){
                if(sizes[i][0] > sizes[i][1]){
                     int tmp = sizes[i][0];
                    sizes[i][0] = sizes[i][1];
                    sizes[i][1] = tmp;
                }                
            }
        }
        
        int max0 = 0, max1=0;
        
        for(int i=0; i<sizes.length; i++){
            if(sizes[i][0] > max0)  max0 = sizes[i][0];
            if(sizes[i][1] > max1)  max1 = sizes[i][1];
        }
        
        rslt = max0*max1;
        return rslt;
    }
}