# author: guoyc
# leetcode url: https://leetcode.com/problems/minimum-path-sum/description/

class Solution(object):
    def minPathSum(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(g)
        n = len(g[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = dp[i - 1][0] + g[i][0] if i - 1 >= 0 else g[i][0]
        for i in range(n):
            dp[0][i] = dp[0][i - 1] + g[0][i] if i - 1 >= 0 else g[0][i]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + g[i][j]

        return dp[m - 1][n - 1]
