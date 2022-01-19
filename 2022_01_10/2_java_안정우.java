class Solution {
    public String solution(int n) {
        String[] nums = {"4","1","2"};
        String answer = "";

        while (n>0) {
            int r = n%3;
            n/=3;
            if (r==0) n--;
            answer = nums[r] + answer;
        }
        return answer;
    }
}
