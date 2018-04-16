class Solution:
    def canIWin(self, choose, total):
        if choose*(choose+1)/2<total: return False
        memo = {}
        def dp(cur, used):
            if used in memo:
                return memo[used]
            else:
                for i in range(choose, 0, -1):
                    if not used&(1<<i):
                        if cur+i>=total: 
                            memo[used] = True
                            return True
                        if not dp(cur+i, used|(1<<i)): 
                            memo[used] = True
                            return True
                memo[used] = False
                return False
        return dp(0, 0)