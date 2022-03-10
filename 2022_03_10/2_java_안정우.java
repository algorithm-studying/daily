class Solution {
    static boolean[] checked;
    static int answer;

    public int solution(String begin, String target, String[] words) {
        checked = new boolean[words.length];
        answer = 0;
        dfs(begin, target, words, 0);
        return answer;
    }

    public static void dfs(String begin, String target, String[] words, int cnt) {

        if (begin.equals(target)) {
            answer = cnt;
            return;
        }

        for (int i=0; i < words.length; i++) {
            // 탐색여부 체크
            if (checked[i]) {
                continue;
            }

            // 탐색조건
            int cntS = 0;
            for (int j=0; j < begin.length(); j++) {
                if (begin.charAt(j) == words[i].charAt(j)) {
                    cntS++;
                }
            }
            // 조건성립시 탐색, 다음으로
            if (cntS == begin.length()-1) {
                checked[i]=true;
                dfs(words[i], target, words, cnt+1);
                checked[i]=false;
            }
        }
    }
}
