class Solution:
    def findTargetSumWays(self, nums, S):
        def dp(i, target):
            if i==-1: return 1 if target==0 else 0
            if (i, target) not in memo:
                memo[(i, target)] = dp(i-1, target-nums[i])+dp(i-1, target+nums[i])
            return memo[(i, target)]
        return dp(len(nums)-1, S)