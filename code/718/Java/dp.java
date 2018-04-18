class Solution {
    public int findLength(int[] A, int[] B) {
        int m=A.length, n=B.length;
        int[][] dp = new int[m][n];
        for (int i=0; i<m; i++)
            dp[i][0] = (A[i]==B[0]?1:0);
        for (int j=0; j<n; j++)
            dp[0][j] = (A[0]==B[j]?1:0);
        for (int i=1; i<m; i++)
            for (int j=1; j<n; j++)
                dp[i][j] = (A[i]==B[j]?(dp[i-1][j-1]+1):0);
        int ret = 0;
        for (int i=0; i<m; i++)
            for (int j=0; j<n; j++)
                ret = (dp[i][j]>ret)?dp[i][j]:ret;
        return ret;
    }
}