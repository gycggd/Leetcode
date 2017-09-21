# author: guoyc
# leetcode url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b = -sys.maxint - 1
        s = 0

        for p in prices:
            b = max(b, -p)
            s = max(s, b + p)

        return s
