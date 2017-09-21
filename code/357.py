# author: guoyc
# leetcode url: https://leetcode.com/problems/count-numbers-with-unique-digits/description/

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 1

        res = 10

        uniq = 9
        avail = 9

        while n > 1 and avail > 0:
            uniq = avail * uniq
            res += uniq
            n -= 1
            avail -= 1

        return res
