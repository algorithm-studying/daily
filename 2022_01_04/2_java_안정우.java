class Solution {
    static int check[][];

    public int solution(int m, int n, int[][] puddles) {
        check = new int[m+1][n+1];
        int answer;
        for (int i=0; i<=m; i++) {
            for (int j=0; j<=n; j++) {
                if (i>0&&j>0) check[i][j] = -1;
            }
        }

        check[1][1] = 1;
        for (int[] puddle : puddles)
            check[puddle[0]][puddle[1]] = 0;

        for (int i=1; i<=m; i++) {
            for (int j=1; j<=n; j++) {
                if (i==1 && j==1) continue;
                else if (check[i][j] >= 0) continue;
                else
                    check[i][j] = check[i-1][j]%1000000007 + check[i][j-1]%1000000007;
            }
        }
        return answer = check[m][n]%1000000007;
    }
}

##방법2.메소드사용
class Solution {
    static int check[][];
    public int solution(int m, int n, int[][] puddles) {
        
        check = new int[m][n];
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                check[i][j] = -1;
            }
        }
        check[0][0] = 1;
        for (int[] puddle : puddles)
            check[puddle[0]-1][puddle[1]-1] = 0;
     
        return dp(m-1,n-1)%1000000007;
    }

    public static int dp(int x, int y) {
        
        if (x<0 || y<0) return 0;
        if (check[x][y] >= 0)
            return check[x][y];
        
        return check[x][y] = dp(x-1,y)%1000000007 + dp(x,y-1)%1000000007;    
    }
}
