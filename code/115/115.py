# author: guoyc
# leetcode url: https://leetcode.com/problems/distinct-subsequences/description/

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(t)
        n = len(s)

        if n == 0:
            return 0

        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            dp[0][i] = (dp[0][i - 1] if i > 0 else 0) + (1 if s[i] == t[0] else 0)

        for i in range(1, m):
            for j in range(i, n):
                if s[j] == t[i]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[m - 1][n - 1]
