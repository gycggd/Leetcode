class Solution:
    def numDecodings(self, s):
        if not s: return 0
        dp = [0]*(len(s)+1)
        dp[-1] = 1
        if s[0]!='0': dp[0]=1
        for i in range(1, len(s)):
            if s[i]!='0': dp[i] += dp[i-1]
            if s[i-1]=='1' or (s[i-1]=='2' and s[i]<='6'): dp[i] += dp[i-2]
        return dp[len(s)-1]