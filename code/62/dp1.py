class Solution:
    def uniquePaths(self, m, n):
        dp = [[0]*n for _ in range(m)]
        for i in range(m): dp[i][0] = 1
        for j in range(n): dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]