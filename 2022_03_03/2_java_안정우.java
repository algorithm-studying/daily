class Solution {
    public int[] solution(int brown, int yellow) {
        int x, y;
        int[] answer = new int[2];
        int xy = brown + yellow;
        for (x=2; x<xy; x++) {
            if (xy%x==0) {
                y = xy/x;
                if (2*(x+y)-4==brown) {
                    answer[0]=x;
                    answer[1]=y;
                }
            }
        }
        return answer;
    }
}
