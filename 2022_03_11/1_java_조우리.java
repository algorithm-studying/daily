class Solution {
    public String solution(int a, int b) {
        int[] arr = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int total = 0;
        String rslt = "";
        
        if(a > 1){
            for(int i=0; i<a-1; i++){
                total += arr[i];
            }
        }
        
        total += b;
        
        int day = total % 7;
        
        switch(day){
            case 1:
                rslt = "FRI";
                break;
            case 2:
                rslt = "SAT";
                break;
            case 3:
                rslt = "SUN";
                break;
            case 4:
                rslt = "MON";
                break;
            case 5:
                rslt = "TUE";
                break;
            case 6:
                rslt = "WED";
                break;
            case 0:
                rslt = "THU";
                break;
        }
        
        return rslt;
    }
}