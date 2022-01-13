import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> que = new LinkedList<Integer>();
        for(int i=0; i<progresses.length; i++){
            if((100-progresses[i])%speeds[i] != 0){
                que.add((100-progresses[i])/speeds[i]+1);
            }
            else{
                que.add((100-progresses[i])/speeds[i]);
            }
        }
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        int prev = que.poll();
        int num = 1;
        
        while(!que.isEmpty()){
            int curr = que.poll();
            if(prev>=curr){
                num++;
            }else{
                list.add(num);
                num = 1;
                prev = curr;
            }
        }
        list.add(num);
        
        int[] rslt = new int[list.size()];
        for(int i=0; i<rslt.length; i++){
            rslt[i] = list.get(i);
        }
        
        return rslt;
    }
}