import java.util.*;

class Solution {
    public long solution(int w, int h) {
        long answer = 1;
        Long width = Long.valueOf(w);
        Long height = Long.valueOf(h);
        long shorter = Math.min(width,height);
        long longer = Math.max(width,height);

        answer = width*height - (width + height - 
                                 GCD(longer, shorter));

        return answer;
    }

    long GCD(long a, long b) {
        if (a%b == 0) {
            return b;
        }
        return GCD(b, a%b);
    }
}
