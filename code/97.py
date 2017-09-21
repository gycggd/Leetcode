# author: guoyc
# leetcode url: https://leetcode.com/problems/interleaving-string/description/

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        if len(s1) + len(s2) != len(s3):
            return False

        letters = [0 for i in range(26)]

        for c in s1:
            letters[ord(c) - ord('a')] += 1
        for c in s2:
            letters[ord(c) - ord('a')] += 1
        for c in s3:
            letters[ord(c) - ord('a')] -= 1

        for i in letters:
            if i != 0:
                return False

        m = len(s1)
        n = len(s2)

        if m == 0:
            return s2 == s3
        if n == 0:
            return s1 == s3

        dp = [[False] * (m + 1) for _ in range(m + n + 1)]
        dp[0][0] = True

        for i in range(m + n):
            for j in range(m + 1):
                if dp[i][j]:
                    if j < m and s3[i] == s1[j]:
                        dp[i + 1][j + 1] = True
                    if i - j < n and s3[i] == s2[i - j]:
                        dp[i + 1][j] = True

        return dp[m + n][m]

#         dp = [False] * (m+1)
#         dp[0] = True

#         for i in range(m+n):
#             next_dp = [False] * (m+1)
#             for j in range(min(m+1, i+1)):
#                 if dp[j]:
#                     if j<m and s3[i]==s1[j]:
#                         next_dp[j+1] = True
#                     if i-j<n and s3[i]==s2[i-j]:
#                         next_dp[j] = True
#             dp = next_dp

#         return dp[m]
