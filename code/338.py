# author: guoyc
# leetcode url: https://leetcode.com/problems/counting-bits/description/

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num + 1)
        dp[0] = 0
        for i in range(num):
            if 2 * i <= num:
                dp[2 * i] = dp[i]
            if 2 * i + 1 <= num:
                dp[2 * i + 1] = dp[i] + 1
        return dp
