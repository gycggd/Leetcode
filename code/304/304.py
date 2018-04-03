# author: guoyc
# leetcode url: https://leetcode.com/problems/range-sum-query-2d-immutable/description/


class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
            self.dp = [[]]
            return

        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = matrix[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + matrix[i][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + matrix[0][i]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = matrix[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

        self.dp = dp
        print dp

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 > row2:
            row1, row2 = row2, row1
        if col1 > col2:
            col1, col2 = col2, col1

        return self.dp[row2][col2] + (self.dp[row1 - 1][col1 - 1] if row1 >= 1 and col1 >= 1 else 0) - (
        self.dp[row2][col1 - 1] if col1 >= 1 else 0) - (self.dp[row1 - 1][col2] if row1 >= 1 else 0)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
