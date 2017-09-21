# author: guoyc
# leetcode url: https://leetcode.com/problems/maximum-subarray/description/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maax = nums[0]
        suum = 0
        for num in nums:
            suum += num
            maax = max(maax, suum)
            if suum < 0:
                suum = 0
        return maax


class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.cal(nums)[0]

    def cal(self, nums):
        if len(nums) == 1:
            return [nums[0]] * 4
        left = nums[:len(nums) / 2]
        right = nums[len(nums) / 2:]
        cal_l = self.cal(left)
        cal_r = self.cal(right)
        max_v = max(cal_l[0], cal_r[0], cal_l[3] + cal_r[2])
        total_v = cal_l[1] + cal_r[1]
        left_v = max(cal_l[2], cal_l[1] + cal_r[2])
        right_v = max(cal_r[3], cal_r[1] + cal_l[3])
        return [max_v, total_v, left_v, right_v]
