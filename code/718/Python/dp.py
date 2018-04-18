class Solution:
    def findLength(self, A, B):
        m, n = len(A), len(B)
        dp = [[0]*n for _ in range(m)]
        ret = 0
        for i in range(m):
            if A[i]==B[0]:
                dp[i][0] = 1
                ret = max(ret, dp[i][0])
        for j in range(n):
            if A[0]==B[j]:
                dp[0][j] = 1
                ret = max(ret, dp[0][j])
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i-1][j-1] + 1) if A[i]==B[j] else 0
                ret = max(dp[i][j], ret)
        return ret