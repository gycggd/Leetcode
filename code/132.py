# author: guoyc
# leetcode url: https://leetcode.com/problems/palindrome-partitioning-ii/description/

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        dp = range(l)

        for i in range(l):
            for j in range(0, min(i + 1, l - i)):
                if s[i - j] == s[i + j]:
                    dp[i + j] = min((dp[i - j - 1] + 1 if i - j - 1 >= 0 else 0), dp[i + j])
                else:
                    break
            for j in range(1, min(i + 2, l - i)):
                if s[i - j + 1] == s[i + j]:
                    dp[i + j] = min((dp[i - j] + 1 if i - j >= 0 else 0), dp[i + j])
                else:
                    break

        return dp[l - 1]
