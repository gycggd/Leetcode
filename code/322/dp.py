class Solution:
    def coinChange(self, coins, amount):
        dp = [sys.maxsize]*(amount+1)
        dp[0] = 0
        for i in range(amount):
            for c in coins:
                if i+c<=amount:
                    dp[i+c] = min(dp[i+c], dp[i]+1)
        return dp[amount] if dp[amount]!=sys.maxsize else -1