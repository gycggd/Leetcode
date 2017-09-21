# author: guoyc
# leetcode url: https://leetcode.com/submissions/detail/113776704/

import sys


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        if k == 0:
            return 0

        if k >= n / 2:
            sum = 0
            for i in range(n - 1):
                sum += (prices[i + 1] - prices[i]) if prices[i + 1] > prices[i] else 0
            return sum

        buy = [-sys.maxint - 1] * k
        sell = [0] * k

        for p in prices:
            for i in reversed(range(k)):
                sell[i] = max(sell[i], buy[i] + p)
                buy[i] = max(buy[i], sell[i - 1] - p if i >= 1 else -p)

        return sell[k - 1]
