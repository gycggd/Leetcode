# author: guoyc
# leetcode url: https://leetcode.com/problems/russian-doll-envelopes/description/

import sys


class Solution(object):
    def maxEnvelopes(self, envs):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envs = sorted(envs, lambda x, y: (x[0] - y[0]) if x[0] != y[0] else (y[1] - x[1]))
        n = len(envs)

        dp = [sys.maxint] * n
        size = 0

        for env in envs:

            i = 0
            while env[1] > dp[i]:
                i += 1
            dp[i] = env[1]
            # can be replaced with binary search

            if i == size:
                size += 1

        return size
