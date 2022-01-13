import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String rslt = "";
        
        HashMap<String, Integer> part = new HashMap<>();
        
        for(String name : participant){
            Integer inte = part.getOrDefault(name, 0);
            part.put(name, ++inte);
        }
        
        for(String name: completion){
            part.put(name, part.get(name)-1);
        }
        
        for(String key : part.keySet()){
            if(part.get(key) != 0){
                rslt = key;
            }
        }
        
        return rslt;
    }
}