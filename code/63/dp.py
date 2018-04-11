class Solution:
    def uniquePathsWithObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        if grid[0][0]==1 or grid[-1][-1]==1: return 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if grid[i][0]==0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if grid[0][j]==0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j]==1:
                    continue
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
