# author: guoyc
# leetcode url: https://leetcode.com/problems/scramble-string/description/

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        length = len(s1)

        letters = [0] * 26

        for i in range(length):
            letters[ord(s1[i]) - ord('a')] += 1
            letters[ord(s2[i]) - ord('a')] -= 1

        for i in letters:
            if i != 0:
                return False

        dp = [[[False] * length for i in range(length)] for i in range(length)]

        for i in range(length):
            for j in range(length - i):
                for k in range(length - i):
                    if i == 0:
                        dp[i][j][k] = (s1[j] == s2[k])
                    for l in range(i):
                        if (dp[l][j][k] and dp[i - l - 1][j + l + 1][k + l + 1]) or (
                                    dp[l][j][k + i - l] and dp[i - l - 1][j + l + 1][k]):
                            dp[i][j][k] = True
                            break

        return dp[length - 1][0][0]
