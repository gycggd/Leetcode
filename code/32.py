# author: guoyc
# leetcode url: https://leetcode.com/problems/longest-valid-parentheses/description/

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        maax = 0

        l = 0
        r = 0
        for c in s:
            if c == '(':
                l += 1
            else:
                r += 1
            if r > l:
                r = 0
                l = 0
            elif r == l:
                maax = max(2 * r, maax)

        l = 0
        r = 0
        for c in s[::-1]:
            if c == ')':
                r += 1
            else:
                l += 1
            if l > r:
                r = 0
                l = 0
            elif r == l:
                maax = max(2 * l, maax)

        return maax
