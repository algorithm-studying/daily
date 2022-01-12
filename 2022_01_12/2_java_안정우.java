import java.util.*;
import java.util.concurrent.ConcurrentLinkedQueue;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> queue = new ConcurrentLinkedQueue<>();
        
        for (int i=0; i<progresses.length;i++) {
            queue.add(
                (100-progresses[i]) % speeds[i] ==0 ?
                (100-progresses[i]) / speeds[i] :
                (100-progresses[i]) / speeds[i] + 1
            );
        }
        ArrayList<Integer> list = new ArrayList<>();
        int prev = queue.poll();
        int numOfFuncs = 1;
        
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            if (prev >= cur) {
                numOfFuncs++;
            } else {
                list.add(numOfFuncs);
                numOfFuncs = 1;
                prev = cur;
            }
        }
        list.add(numOfFuncs);
        
        int[] answer = new int[list.size()];
        for (int k=0; k<list.size();k++) {
            answer[k] = list.get(k);
        }
        return answer;
    }
}
