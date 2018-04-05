class Solution:
    def maxSubArray(self, nums):
        if not nums: return 0
        dp = [0]*len(nums)
        for i in range(len(nums)):
            if i==0 or dp[i-1]<0: dp[i] = nums[i]
            else: dp[i] = dp[i-1]+nums[i]
        return max(dp)