class Solution:
    def minPathSum(self, grid):
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        dp = [0]*n
        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = dp[i-1]+grid[0][i]
        for _ in range(1, m):
            for i in range(n):
                dp[i] = min(dp[i], dp[i-1] if i-1>=0 else sys.maxsize)+grid[_][i]
        return dp[n-1]