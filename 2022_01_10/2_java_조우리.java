class Solution {
    public String solution(int n) {
        String rslt = "";
        
        while(n != 0){
            int r = n%3;
            n=n/3;
            
            if(r==0){
                n--;
                r = 4;
            }
            rslt = String.valueOf(r) + rslt;
        }
        return rslt;
    }
}