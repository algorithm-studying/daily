class Solution {
    public String solution(String phone_number) {
        char[] arr = phone_number.toCharArray();
        String rslt = "";
        
        for(int i=0; i<arr.length-4; i++){
            rslt += "*";
        }
        
        for(int i=arr.length-4; i<arr.length; i++){
            rslt += String.valueOf(arr[i]);
        }
        
        return rslt;
    }
}