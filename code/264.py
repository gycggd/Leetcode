# author: guoyc
# leetcode url: https://leetcode.com/problems/ugly-number-ii/description/

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1] * n

        i1 = i2 = i3 = 0

        for i in range(1, n):
            res[i] = min(res[i1] * 2, res[i2] * 3, res[i3] * 5)
            if res[i] == res[i1] * 2:
                i1 += 1
            if res[i] == res[i2] * 3:
                i2 += 1
            if res[i] == res[i3] * 5:
                i3 += 1

        return res[n - 1]
