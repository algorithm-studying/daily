import java.util.*;

class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        Integer left = 11;
        Integer right = 13;
        Integer[] le = {1,4,7,11};
        Integer[] ri = {3,6,9,13};
        Integer[] ce = {2,5,8,0};

        Integer leftPos = -1;
        Integer rightPos = 1;

        for (Integer i : numbers) {
            System.out.print(left);
            System.out.print(",");
            System.out.println(right);
            if (i==1||i==4||i==7) {
                answer+="L";
                left = i;
                leftPos = -1;
            }
            else if (i==3||i==6||i==9) {
                answer+="R";
                right = i;
                rightPos = 1;
            } 
            else {
                Integer pgL = 0;
                Integer pgR = 0;
                if (leftPos == 0 && rightPos == 0) {
                    pgL = positiongap(ce, ce, left, i);
                    pgR = positiongap(ce, ce, right, i);
                }
                else if (leftPos == -1 && rightPos == 0) {
                    pgL = positiongap(le, ce, left, i)+1;
                    pgR = positiongap(ce, ce, right, i);
                }
                else if (leftPos == 0 && rightPos == 1) {
                    pgL = positiongap(ce, ce, left, i);
                    pgR = positiongap(ri, ce, right, i)+1;
                }
                else {
                    pgL = positiongap(le, ce, left, i)+1;
                    pgR = positiongap(ri, ce, right, i)+1;
                }
               
                if (pgL<pgR) {
                    answer+="L";
                    left = i;
                    leftPos = 0;
                }
                else if (pgL>pgR){
                    answer+="R";
                    right = i;
                    rightPos = 0;
                }
                else {
                    if (hand.equals("left")) {
                        answer+="L";
                        left = i;
                        leftPos = 0;
                    }
                    else {
                        answer+="R";
                        right = i;
                        rightPos = 0;
                    }
                }
            }
        }
        return answer;
    }
    public Integer positiongap(Integer[] a, Integer[] b, Integer c, Integer d) {
        return Math.abs(Arrays.asList(a).indexOf(c)-Arrays.asList(b).indexOf(d));
    }
}
