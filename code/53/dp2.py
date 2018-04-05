class Solution:
    def maxSubArray(self, nums):
        s, ret = 0, -sys.maxsize
        for n in nums:
            if s<0: s = n
            else: s += n
            ret = max(ret, s)
        return ret