class Solution:
    def uniquePaths(self, m, n):
        dp = [1]*n
        for i in range(m-1):
            for j in range(n):
                dp[j] += (dp[j-1] if j-1>=0 else 0)
        return dp[-1]