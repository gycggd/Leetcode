class Solution:
    def isScramble(self, s1, s2):
        if len(s1)!=len(s2): return False
        N = len(s1)
        dp = [[[False]*N for _ in range(N)] for _ in range(N+1)]
        for l in range(1, N+1):
            for i in range(N-l+1):
                for j in range(N-l+1):
                    if dp[l][i][j]: continue
                    if s1[i:i+l]==s2[j:j+l]:
                        dp[l][i][j] = True
                        continue
                    for k in range(1, l):
                        if dp[k][i][j] and dp[l-k][i+k][j+k]:
                            dp[l][i][j] = True
                            break
                        if dp[k][i][j+l-k] and dp[l-k][i+k][j]:
                            dp[l][i][j] = True
                            break
        return dp[N][0][0]