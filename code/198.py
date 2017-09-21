# author: guoyc
# leetcode url: https://leetcode.com/problems/house-robber/description/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * n

        for i in range(n):
            dp[i] = max(dp[i - 1] if i - 1 >= 0 else 0, (dp[i - 2] if i - 2 >= 0 else 0) + nums[i])

        return dp[n - 1]
