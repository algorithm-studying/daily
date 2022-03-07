class Solution {
    public long solution(int a, int b) {
        long rslt = 0;
        
        if(a == b){
            rslt = a;
        }else if(a>b){
            for(int i=b; i<=a; i++){
                rslt += i;
            }
        }
        else{
            for(int i=a; i<=b; i++){
                rslt += i;
            }
        }
        return rslt;
    }
}