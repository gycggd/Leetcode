# author: guoyc
# leetcode url: https://leetcode.com/problems/word-break/description/

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        l = len(s)
        dp = [False] * (l + 1)
        dp[0] = True

        for i in range(1, l + 1):
            dp[i] = any(dp[j] and s[j:i] in wordDict for j in reversed(range(i)))

        return dp[l]
