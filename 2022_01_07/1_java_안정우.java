import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int[] fail = new int[N];
        Double[] failRate = new Double[N];
        Double[] failRank = new Double[N];
        int total = stages.length;
        
        for (int i = 0; i < N; i++) {
            int a = 0;
            fail[i] = i+1;
            for (int j : stages) {
                if (j == fail[i]) {
                    a++;
                }
            }
            if (total==0) failRate[i] = 0.0;          // stage 도달 유저 없는 경우 실패율 0으로
            else failRate[i] = (1.0*a) / (1.0*total);
            total -= a;
        }
        failRank = failRate.clone();
        
        Arrays.sort(failRank,Collections.reverseOrder());

        for(int i = 0; i < N; i++) {
            answer[i]=Arrays.asList(failRate).indexOf(failRank[i])+1;
            failRate[answer[i]-1]=-1.0;
        }
        return answer;
    }
}
