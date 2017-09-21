# author: guoyc
# leetcode url: https://leetcode.com/problems/burst-balloons/description/

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        new_nums = [1]
        new_nums.extend(nums)
        new_nums.append(1)
        nums = new_nums

        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for i in range(2, n):
            for j in range(n - i):
                for k in range(j + 1, j + i):
                    dp[j][j + i] = max(dp[j][j + i], nums[j] * nums[j + i] * nums[k] + dp[j][k] + dp[k][j + i])

        return dp[0][n - 1]
