class Solution {
    public String solution(String s) {
        String rslt = "";
        int cnt = 0;
        
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c == ' '){
                cnt = 0;
                rslt += String.valueOf(c);
            }else{
                if(cnt %2 == 0){
                    rslt += String.valueOf(c).toUpperCase();
                    cnt++;
                }else{
                    rslt += String.valueOf(c).toLowerCase();
                    cnt++;
                }
            }
        }
        return rslt;
    }
}