class Solution {
    public int solution(int[] a, int[] b) {
        int rslt = 0;
        for(int i=0; i<a.length; i++){
            rslt += a[i] * b[i];
        }
        
        return rslt;
    }
}