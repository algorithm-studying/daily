class Solution {
    public int solution(int[] numbers) {
        int sum = 0;
        
        int[] empty = new int[10];
        
        for(int i=0; i<numbers.length; i++){
            empty[numbers[i]]++;
        }
        
        for(int i=0; i<empty.length; i++){
            if(empty[i] == 0)   sum += i;
        }
        return sum;
    }
}