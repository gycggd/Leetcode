# author: guoyc
# leetcode url: xxx

class Solution(object):
    def minDistance(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(w1)
        n = len(w2)

        dp = [0] * (n + 1)

        for i in range(n + 1):
            dp[i] = i

        for i in range(1, m + 1):
            pre = dp[0]
            dp[0] += 1
            for j in range(1, n + 1):
                if w1[i - 1] == w2[j - 1]:
                    tmp = dp[j]
                    dp[j] = pre
                    pre = tmp
                else:
                    tmp = dp[j]
                    dp[j] = 1 + min(dp[j - 1], pre, dp[j])
                    pre = tmp
        return dp[n]


class Solution2(object):
    def minDistance(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(w1)
        n = len(w2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp.pop()
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if w1[i - 1] == w2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
