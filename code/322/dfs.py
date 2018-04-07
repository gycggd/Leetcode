class Solution:
    ret = sys.maxsize
    def coinChange(self, coins, amount):
        coins.sort()
        def dfs(target, i, cnt):
            if i<0 or target<0 or cnt>=self.ret: return
            q = target//coins[i]
            if target%coins[i]==0:
                self.ret = min(self.ret, cnt+q)
                return
            if q+cnt+1>=self.ret: return
            dfs(target-coins[i], i, cnt+1)
            dfs(target, i-1, cnt)
        dfs(amount, len(coins)-1, 0)
        return self.ret if self.ret<sys.maxsize else -1