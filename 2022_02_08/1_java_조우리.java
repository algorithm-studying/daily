class Solution {
    public boolean solution(String s) {
        boolean rslt = true;
        char[] arr = s.toCharArray();
        
        int size = arr.length;
        
        if(size != 4 && size != 6){
            rslt = false;
        }else{
            for(int i=0; i<arr.length; i++){ //48~57
                if(arr[i] <= '9' && arr[i]>= '0'){
                    rslt = true;
                    continue;
                }else{
                    rslt = false;
                    break;
                }
            }
        }
        
        return rslt;
    }
}