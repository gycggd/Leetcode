class Solution:
    def minPathSum(self, grid):
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] = grid[i-1][0]+grid[i][0]
        for i in range(1, n):
            grid[0][i] = grid[0][i-1]+grid[0][i]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
        return grid[-1][-1]