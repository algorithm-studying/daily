class Solution {
    public long solution(int price, int money, int count) {
        long total = 0;
        
        for(int i=1; i<= count; i++){
            total += (long)(price * i);
        }
        
        long rslt = (long)(total-money);
        
        if(rslt <= 0)   return 0;
        else    return rslt;
    }
}