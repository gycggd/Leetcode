# author: guoyc
# leetcode url: https://leetcode.com/problems/regular-expression-matching/

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0

        if len(p) == 1:
            return len(s) == 1 and (p == '.' or p == s)

        if p[1] != '*':
            return len(s) > 0 and (p[0] == '.' or p[0] == s[0]) and self.isMatch(s[1:], p[1:])

        if self.isMatch(s, p[2:]):
            return True

        while len(s) > 0 and (p[0] == '.' or s[0] == p[0]):
            if self.isMatch(s[1:], p[2:]):
                return True
            s = s[1:]

        return False
