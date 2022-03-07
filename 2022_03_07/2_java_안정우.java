class Solution {
    public int solution(String s) {
        int answer = s.length();

        // 압축단위 : 1 ~ 문자열길이절반까지
        for (int i = 1; i <= s.length() / 2; i++) {
            int cnt = 1;
            String zip = s.substring(0, i);
            StringBuilder newS = new StringBuilder();

            for (int j = i; j <= s.length(); j += i) {
                String next = "";
                if (j+i > s.length()) {
                    next = s.substring(j, s.length());
                }
                else {
                    next = s.substring(j, j+i);
                }

                if (zip.equals(next)) cnt++;
                else {
                    newS.append((cnt != 1 ? cnt : "") + zip);
                    zip = next;
                    cnt = 1;
                }
            }
            newS.append(zip);
            answer = Math.min(answer, newS.length());
        }
        return answer;
    }
}
