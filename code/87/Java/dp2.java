class Solution {
    public boolean isScramble(String s1, String s2) {
        if (s1.length()!=s2.length()) {
            return false;
        }
        int N = s1.length();
        boolean dp[][][] = new boolean[N+1][N][N];
        boolean hasLen[] = new boolean[N+1];
        
        for (int l=1; l<N+1; l++) {
            for (int i=0; i<N-l+1; i++) {
                for (int j=0; j<N-l+1; j++) {
                    if (dp[l][i][j])
                        continue;
                    if (s1.substring(i, i+l).equals(s2.substring(j, j+l))) {
                        dp[l][i][j] = true;
                        hasLen[l] = true;
                        continue;
                    }
                    for (int k=1; k<l; k++) {
                        if (!hasLen[k] || !hasLen[l-k]) {
                            continue;
                        }
                        if (dp[k][i][j] && dp[l-k][i+k][j+k]) {
                            dp[l][i][j] = true;
                            hasLen[l] = true;
                            break;
                        }
                        if (dp[k][i][j+l-k] && dp[l-k][i+k][j]) {
                            dp[l][i][j] = true;
                            hasLen[l] = true;
                            break;
                        }
                    }
                    
                }
            }
        }
        return dp[N][0][0];
    }
}