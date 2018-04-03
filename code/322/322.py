# author: guoyc
# leetcode url: https://leetcode.com/problems/coin-change/description/

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for c in coins:
            if c <= amount:
                dp[c] = 1

        for i in range(amount):
            if dp[i] != -1:
                for c in coins:
                    if i + c <= amount:
                        if dp[i + c] == -1:
                            dp[i + c] = dp[i] + 1
                        else:
                            dp[i + c] = min(dp[i] + 1, dp[i + c])

        return dp[amount]
