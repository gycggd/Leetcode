# author: guoyc
# leetcode url: https://leetcode.com/problems/maximum-product-subarray/description/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxium = [0] * n
        minimum = [0] * n

        maxium[0] = minimum[0] = nums[0]

        for i in range(1, n):
            maxium[i] = max(maxium[i - 1] * nums[i], minimum[i - 1] * nums[i], nums[i])
            minimum[i] = min(maxium[i - 1] * nums[i], minimum[i - 1] * nums[i], nums[i])

        print maxium
        print minimum
        return max(maxium)
