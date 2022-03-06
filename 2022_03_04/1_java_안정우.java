class Solution {
    public String solution(int n) {
        String answer = "";
        int cnt = n/2;
        if (n%2==0) {
            answer = "수박".repeat(cnt);
        }
        else answer = "수박".repeat(cnt) + "수";
        return answer;
    }
}
