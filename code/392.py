# author: guoyc
# leetcode url: https://leetcode.com/problems/is-subsequence/description/

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for c in s:
            idx = t.find(c)
            if idx != -1:
                t = t[idx + 1:]
            else:
                return False

        return True
