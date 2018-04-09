class Solution:
    def maxProduct(self, nums):
        maximum = [0]*len(nums)
        minimum = [0]*len(nums)
        maximum[0], minimum[0], ret = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            maximum[i] = max(nums[i], maximum[i-1]*nums[i], minimum[i-1]*nums[i])
            minimum[i] = min(nums[i], maximum[i-1]*nums[i], minimum[i-1]*nums[i])
            ret = max(maximum[i], ret)
        return ret