class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total&1: return False
        target = total>>1
        dp = [False]*(target+1)
        dp[0] = True
        for n in nums:
            for i in range(target, n-1, -1):
                dp[i] |= dp[i-n]
        return dp[target]