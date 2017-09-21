# author: guoyc
# leetcode url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)

        if n < 2:
            return 0

        buy = -prices[0]
        sell = cool = 0

        for i in range(1, n):
            pre_buy, pre_sell, pre_cool = buy, sell, cool
            buy = max(pre_cool - prices[i], pre_buy)
            sell = max(pre_sell, pre_buy + prices[i])
            cool = max(pre_cool, pre_sell)

        return sell
