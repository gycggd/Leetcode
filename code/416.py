# author: guoyc
# leetcode url: https://leetcode.com/problems/partition-equal-subset-sum/discuss/

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        suum = sum(nums)

        if suum % 2 == 1:
            return False

        suum /= 2

        n = len(nums)

        dp = [False for j in range(suum + 1)]

        dp[0] = True

        for i in range(n):
            for j in reversed(range(suum + 1)):
                dp[j] = dp[j] or (j >= nums[i] and dp[j - nums[i]])

        return dp[suum]
