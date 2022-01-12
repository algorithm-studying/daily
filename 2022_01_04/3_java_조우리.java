class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] dp = new int[n+1][m+1];
        
        for(int i=0; i<puddles.length; i++){
            dp[puddles[i][1]][puddles[i][0]] = -1;
        }
        
        dp[1][1] = 1;
        
        for(int i=1; i<=n; i++){
            for(int j=1; j<=m; j++){
                if(dp[i][j] ==-1)   continue;
                if(i-1>0 && dp[i-1][j] != -1) dp[i][j] += dp[i-1][j]%1000000007;
                if(j-1>0 && dp[i][j-1] != -1) dp[i][j] += dp[i][j-1]%1000000007;
            }
        }
        
        return dp[n][m]%1000000007;
    }
}