import java.util.*;

class Solution {
    public int[] solution(String s) {

        ArrayList<String> arr = new ArrayList<>();

        // 1. 겉에 {{}} 삭제
        s = s.substring(2,s.length()-2);

        // 2. 배열 표시하는 문자열 공백으로 대체
        s = s.replace("},{"," ");

        // 3. 공백 기준으로 쪼개서 배열에 넣기
        String[] str = s.split(" ");

        // 4. 문자열길이 기준으로 정렬
        Arrays.sort(str,new Comparator<String>(){
            public int compare(String s1, String s2){
                return s1.length() - s2.length();
            }
        });

        // 5. 정렬된 배열내에서 원소를 "," 기준으로 나누어, 해당원소를 포함하지 않으면 arraylist에 추가
        for (String a : str) {
            String[] tmp = a.split(",");
            for (String b : tmp) {
                if (!arr.contains(b)) arr.add(b);
            }
        }

        // 6. arraylist -> 배열 형변환
        String[] asw = arr.toArray(new String[arr.size()]);
        int[] answer = new int[asw.length];

        for (int i = 0; i < asw.length; i++) {
            answer[i] = Integer.parseInt(asw[i]);
        }
        return answer;
    }
}
