# author: guoyc
# leetcode url: https://leetcode.com/problems/continuous-subarray-sum/discuss/

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        dic = {0: -1}

        suum = 0

        for i in range(len(nums)):
            suum += nums[i]
            if k != 0:
                suum %= k
            if dic.has_key(suum):
                if i - dic[suum] > 1:
                    return True
            else:
                dic[suum] = i

        return False
