class Solution {
    public int solution(int n) {
        int answer = 0;
        String num = "";
        int rslt = 0;
        if(n < 3){
            answer=n;
        }
        else{
            while(n > 0){
                num = (n%3) + num;
                n = n/3;
            }
            
            num = new StringBuilder(num).reverse().toString();
            answer = Integer.parseInt(num, 3);
        }
        return answer;
    }
}