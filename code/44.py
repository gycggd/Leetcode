# author: guoyc
# leetcode url: https://leetcode.com/problems/wildcard-matching/description/

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)

        if n == 0:
            return m == 0

        dp = [[False for i in range(n + 1)] for j in range(m + 1)]

        dp[0][0] = True

        if p[0] == '*':
            for i in range(m + 1):
                dp[i][0] = True

        for j in range(n):
            if p[j] == '*':
                dp[0][j + 1] = True
            else:
                break

        for i in range(m):
            for j in range(n):
                if p[j] != '*':
                    if dp[i][j] and (p[j] == '?' or p[j] == s[i]):
                        dp[i + 1][j + 1] = True
                else:
                    if dp[i][j + 1] or dp[i + 1][j]:
                        dp[i + 1][j + 1] = True

        return dp[m][n]
