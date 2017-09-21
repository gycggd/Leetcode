# author: guoyc
# leetcode url: https://leetcode.com/problems/unique-binary-search-trees/description/

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        dp = [0 for _ in range(n + 1)]

        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]
