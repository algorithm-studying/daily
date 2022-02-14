import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int cnt = 0;
        for(int i=0; i<arr.length; i++){
            if(arr[i] % divisor ==0)    cnt++;
        }
        
        int[] rslt = new int[cnt];
        int num = 0;
        
        for(int i=0; i<arr.length; i++){
            if(arr[i] %divisor ==0){
                rslt[num] = arr[i];
                num++;
            }
        }
        if(cnt ==0){
            int[] rslt2 = {-1};
            return rslt2;
        }else{
            Arrays.sort(rslt);
            return rslt;
        }
    }
}