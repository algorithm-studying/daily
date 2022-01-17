import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;

        Arrays.sort(lost);
        Arrays.sort(reserve);
        for (int i = 0; i<lost.length; i++) {
            for (int j = 0; j<reserve.length; j++) {
                if (lost[i] == reserve[j] ) {
                    answer += 1;
                    lost[i] = -1;
                    reserve[j] = -1;
                    break;
                }
            }
        }
        for (int i = 0; i<lost.length; i++) {
            for (int j = 0; j<reserve.length; j++) {
                System.out.println(reserve[j]);
                if (lost[i] - reserve[j] == -1 || lost[i] - reserve[j] == 1) {
                    lost[i] = -1;
                    answer += 1;
                    reserve[j] = -1;
                    break;
                }
            }
        }
        return n-(lost.length-answer);
    }
}


// 다른사람 풀이

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] people = new int[n];
        int answer = n;

        for (int l : lost) 
            people[l-1]--;
        for (int r : reserve) 
            people[r-1]++;

        for (int i = 0; i < people.length; i++) {
            if(people[i] == -1) {
                if(i-1>=0 && people[i-1] == 1) {
                    people[i]++;
                    people[i-1]--;
                }else if(i+1< people.length && people[i+1] == 1) {
                    people[i]++;
                    people[i+1]--;
                }else 
                    answer--;
            }
        }
        return answer;
    }
}
