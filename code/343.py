# author: guoyc
# leetcode url: https://leetcode.com/problems/integer-break/description/

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        mod = n % 3
        if mod == 0:
            return 3 ** int(n / 3)
        elif mod == 1:
            return 3 ** int(n / 3 - 1) * 4
        else:
            return 3 ** int(n / 3) * 2
