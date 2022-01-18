mport java.util.*;

class Solution {
    public int solution(String name) {
        int answer = 0;
        int leRi = name.length()-1;
        
        for (int i = 0; i < name.length(); i++) {
            
            answer += Math.min(90 - (int)name.toCharArray()[i]+1, 
                              (int)name.toCharArray()[i] - 65); 
            
            int nextIdx = i + 1;
            while (nextIdx < name.length() && name.charAt(nextIdx) == 'A') {
                nextIdx++;
            }
            int notA = name.length() - (nextIdx - i);
            int min = Math.min(i, name.length() - nextIdx);
            
            leRi = Math.min(leRi, min + notA);
            
            
        }
        answer += leRi;
        return answer;
    }
}
