# author: guoyc
# leetcode url: https://leetcode.com/problems/palindromic-substrings/description/


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        dp = [[False for _ in range(n)] for __ in range(n)]

        count = 0

        for i in range(n):
            dp[i][i] = True
            count += 1

        for l in range(1, n):
            for i in range(n - l):
                dp[i][i + l] = (s[i] == s[i + l]) and (dp[i + 1][i + l - 1] if i + 1 <= i + l - 1 else True)
                if dp[i][i + l]:
                    count += 1
        return count
