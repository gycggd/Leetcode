# author: guoyc
# leetcode url: https://leetcode.com/problems/perfect-squares/description/

import math, sys


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [sys.maxint] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            sr = int(math.sqrt(i))
            if sr * sr == i:
                dp[i] = 1
                continue
            for j in range(1, sr + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[-1]


class Solution2(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        mem = {1: 1}

        def f(m):

            if m in mem:
                return mem[m]

            r = int(math.sqrt(m))

            if r * r == m:
                mem[m] = 1
                return 1
            else:
                res = sys.maxint
                for i in reversed(xrange(1, r + 1)):
                    res = min(res, 1 + f(m - i * i))
                    if res == 2:
                        break

                mem[m] = res
                return res

        return f(n)


class Solution3(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Based on Lagrange's Four Square theorem, there
        # are only 4 possible results: 1, 2, 3, 4.

        def isSquare(number):
            sr = int(math.sqrt(number))
            if sr * sr == number:
                return True
            else:
                return False

        if isSquare(n):
            return 1

        # The result is 4 if and only if n can be written in the
        # form of 4^k*(8*m + 7). Please refer to
        # Legendre's three-square theorem.
        tmp = n
        while tmp & 3 == 0:
            tmp >>= 2
        if tmp & 7 == 7:
            return 4

        for i in range(1, int(math.sqrt(n)) + 1):
            if isSquare(n - i * i):
                return 2

        return 3
