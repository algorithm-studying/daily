class Solution {
    public long solution(int w, int h) {
        long answer;
        long W = w;
        long H = h;
        long a = W, b = H, c;
        
        while(b!=0){
            c = a%b;
            a=b;
            b=c;
        }
        
        answer = W*H - a*(W/a + H/a -1);
        
        return answer;
    }
}