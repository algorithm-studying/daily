class Solution {
    boolean solution(String s) {
        boolean rslt = true;
        char[] arr = s.toCharArray();
        
        int pnum = 0;
        int ynum = 0;
        
        for(int i=0; i<arr.length; i++){
            if(arr[i] == 'p' || arr[i] == 'P')  pnum++;
            if(arr[i] == 'y' || arr[i] == 'Y')  ynum++;
        }
        
        if(pnum == ynum)    rslt = true;
        else    rslt = false;

        return rslt;
    }
}