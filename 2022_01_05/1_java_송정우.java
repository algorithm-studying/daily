import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        ArrayList<Integer> temp = new ArrayList<Integer>();
        int[] answer = new int[commands.length];
        int startNum, endNum, pickNum, cnt = 0;
        
        for(int[] command: commands) {
        	if(temp.size() > 0) {
        		temp.removeAll(temp);
        	}
        	
            startNum = command[0] - 1;
            endNum = command[1];
            pickNum = command[2] - 1;
                        
            for(int i = startNum; i < endNum; i++) {
                temp.add(array[i]);
            }
            Collections.sort(temp);
           
            answer[cnt] = temp.get(pickNum);
            cnt++;
        }
                
        return answer;
    }
}

/* 다른 사람 풀이
import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for(int i=0; i<commands.length; i++){
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
        }

        return answer;
    }
}
*/