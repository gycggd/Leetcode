# author: guoyc
# leetcode url: https://leetcode.com/problems/arithmetic-slices/description/


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)

        if n < 3:
            return 0

        count = [2]

        gap = A[1] - A[0]

        for i in range(1, n - 1):
            if A[i + 1] - A[i] == gap:
                count[-1] += 1
            else:
                count.append(2)
                gap = A[i + 1] - A[i]

        print count

        res = 0
        for c in count:
            res += 0 if c <= 2 else (c - 1) * (c - 2) / 2

        return res
