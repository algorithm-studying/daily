class Solution {
    public String solution(String s) {
        String rslt = "";
        char[] arr = s.toCharArray();
        
        if(arr.length % 2==0){
            rslt += String.valueOf(arr[arr.length/2-1]) + String.valueOf(arr[arr.length/2]);
        }else{
            rslt += String.valueOf(arr[arr.length/2]);
        }
        
        return rslt;
    }
}