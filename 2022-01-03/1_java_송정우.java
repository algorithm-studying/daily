class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int ans = 0;

        for(int i = 0; i < numbers.length; i++) 
            answer += numbers[i];
        ans = 45 - answer;
            
        return ans;
    }
}

/* 다른 풀이
class Solution {
    public int solution(int[] numbers) {
        int sum = 45;
        for (int i : numbers) {
            sum -= i;
        }
        return sum;
    }
}
*/