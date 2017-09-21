# author: guoyc
# leetcode url: https://leetcode.com/problems/dungeon-game/description/

import sys

class Solution(object):
    def calculateMinimumHP(self, dd):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dd)
        n = len(dd[0])

        dp = [[sys.maxint] * n for i in range(m)]
        dp[m - 1][n - 1] = 1

        for i in reversed(range(m - 1)):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dd[i + 1][n - 1], 1)

        for i in reversed(range(n - 1)):
            dp[m - 1][i] = max(dp[m - 1][i + 1] - dd[m - 1][i + 1], 1)

        for i in reversed(range(m - 1)):
            for j in reversed(range(n - 1)):
                dp[i][j] = max(min(dp[i + 1][j] - dd[i + 1][j], dp[i][j + 1] - dd[i][j + 1]), 1)

        return max(dp[0][0] - dd[0][0], 1)
