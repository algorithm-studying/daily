class Solution
{
    public int solution(int []A, int []B)
    {
        Arrays.sort(A);
        Arrays.sort(B);
        
        int total = 0;
        
        for(int i=0; i<A.length; i++){
            total += A[i] * B[B.length-i-1];
        }
        
        return total;
    }
}