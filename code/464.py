# author: guoyc
# leetcode url: https://leetcode.com/problems/can-i-win/description/

class Solution(object):
    def canIWin(self, mi, dt):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        mem = {}

        if mi * (mi + 1) / 2 < dt:
            return False

        def helper(nums, total):
            key = str(nums)
            if mem.has_key(key):
                return mem[key]
            if nums[-1] >= total:
                mem[key] = True
                return True
            for i in range(len(nums)):
                if not helper(nums[:i] + nums[i + 1:], total - nums[i]):
                    mem[key] = True
                    return True
            mem[key] = False
            return False

        return helper(range(1, mi + 1), dt)
