# author: guoyc
# leetcode url: https://leetcode.com/problems/maximum-length-of-pair-chain/description/

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        n = len(pairs)
        pairs = sorted(pairs, cmp=lambda x, y: x[0] - y[0])

        ret = 0
        i = n - 1
        while i >= 0:
            ret += 1
            start = pairs[i][0]
            while i - 1 >= 0 and pairs[i - 1][1] >= start:
                i -= 1
            i -= 1

        return ret
