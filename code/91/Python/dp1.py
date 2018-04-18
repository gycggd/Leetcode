class Solution:
    def numDecodings(self, s):
        if not s: return 0
        memo = {}
        def cnt(s, i):
            if i not in memo:
                if i>len(s): ret = 0
                elif i==len(s): ret = 1
                elif s[i]=='0': ret = 0
                elif s[i]=='1' or (s[i]=='2' and i+1<len(s) and s[i+1]<='6'): ret = cnt(s, i+1)+cnt(s,i+2)
                else: ret = cnt(s, i+1) # s[i]>'2'
                memo[i] = ret
            return memo[i]
        return cnt(s, 0)
        