# author: guoyc
# leetcode url: https://leetcode.com/problems/maximal-square/description/


class Solution(object):
    def maximalSquare(self, mat):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(mat)
        if m == 0:
            return 0
        n = len(mat[0])

        if not any(mat[i][j] == '1' for i in range(m) for j in range(n)):
            return 0

        maxlength = 1

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = (mat[i][0] == '1')

        for i in range(n):
            dp[0][i] = (mat[0][i] == '1')

        for i in range(1, m):
            for j in range(1, n):
                if mat[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxlength = max(maxlength, dp[i][j])
        return maxlength * maxlength
