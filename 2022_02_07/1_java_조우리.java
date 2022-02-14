import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int num = 0;
        int tmp = arr[0];
        for(int i=1; i<arr.length; i++){
            if(arr[i] ==tmp)    continue;
            else{
                tmp = arr[i];
                num++;
            }
        }
        
        tmp = arr[0];
        int[] rslt = new int[num+1];
        int cnt = 1;
        rslt[0] = arr[0];
        for(int i=1; i<arr.length; i++){
            if(arr[i] ==tmp)    continue;
            else{
                rslt[cnt] = arr[i];
                tmp = arr[i];
                cnt++;
            }
        }
        
        return rslt;
    }
}