# author: guoyc
# leetcode url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b1 = b2 = -sys.maxint - 1
        s1 = s2 = 0

        for p in prices:
            s2 = max(s2, b2 + p)
            b2 = max(b2, s1 - p)
            s1 = max(s1, b1 + p)
            b1 = max(b1, -p)

        return s2
