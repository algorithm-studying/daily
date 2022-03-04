class Solution {
    public String solution(int n) {
        String rslt = "";
        
        for(int i=1; i<=n; i++){
            if(i%2==0)  rslt += "박";
            else    rslt += "수";
        }
        return rslt;
    }
}