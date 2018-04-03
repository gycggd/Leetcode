# author: guoyc
# leetcode url: https://leetcode.com/problems/decode-ways/description/


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1 if self.isValid(s) else 0

        dp = [0] * len(s)
        dp[0] = 1 if self.isValid(s[0]) else 0
        if self.isValid(s[0]) and self.isValid(s[1]):
            dp[1] += 1
        if self.isValid(s[:2]):
            dp[1] += 1

        for i in range(2, len(s)):
            if self.isValid(s[i]):
                dp[i] += dp[i - 1]
            if self.isValid(s[i - 1:i + 1]):
                dp[i] += dp[i - 2]

        return dp[-1]

    def isValid(self, s):
        if s[0] == '0':
            return False
        return int(s) >= 1 and int(s) <= 26
