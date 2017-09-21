# author: guoyc
# leetcode url: https://leetcode.com/problems/unique-paths-ii/description/

class Solution(object):
    def uniquePathsWithObstacles(self, og):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(og)
        m = len(og[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(m):
            if og[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        for i in range(n):
            if og[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) if og[i][j] == 0 else 0
        return dp[n - 1][m - 1]
