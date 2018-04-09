class Solution:
    def maxProduct(self, nums):
        maximum, minimum, ret = [nums[0]]*3
        for n in nums[1:]:
            maximum, minimum = max(n, n*maximum, n*minimum), min(n, n*maximum, n*minimum)
            ret = max(maximum, ret)
        return ret