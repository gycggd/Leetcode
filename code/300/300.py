# author: guoyc
# leetcode url: https://leetcode.com/problems/longest-increasing-subsequence/description/

import sys


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [sys.maxint] * n

        l = 0

        for num in nums:
            tmp = 0
            while dp[tmp] < num:
                tmp += 1
            dp[tmp] = num
            if tmp == l:
                l += 1

        return l


class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        size = 0

        dp = [sys.maxint] * m

        for n in nums:
            l = 0
            r = size
            while l < r:
                mid = (l + r) / 2
                if dp[mid] < n:
                    l = mid + 1
                else:
                    r = mid
            dp[l] = n
            if l == size:
                size += 1

        return size
