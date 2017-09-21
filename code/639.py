# author: guoyc
# leetcode url: https://leetcode.com/problems/decode-ways-ii/description/

class Solution(object):
    def numDecodings(self, ss):
        """
        :type s: str
        :rtype: int
        """

        def cnt(s):
            if len(s) == 1:
                if s == '0':
                    return 0
                elif s == '*':
                    return 9
                else:
                    return 1
            elif len(s) == 2:
                if s[0] == '0':
                    return 0
                elif s[0] == '*':
                    if s[1] == '*':
                        return 15
                    elif s[1] <= '6':
                        return 2
                    else:
                        return 1
                elif s[0] > '2':
                    return 0
                elif s[0] == '2':
                    if s[1] == '*':
                        return 6
                    elif s[1] > '6':
                        return 0
                    else:
                        return 1
                else:
                    if s[1] == '*':
                        return 9
                    else:
                        return 1
            else:
                return 0

        if len(ss) < 2:
            return cnt(ss)

        dp0 = cnt(ss[0])
        dp1 = dp0 * cnt(ss[1]) + cnt(ss[:2])

        for i in range(2, len(ss)):
            dp2 = cnt(ss[i]) * dp1 + cnt(ss[i - 1:i + 1]) * dp0
            dp0, dp1 = dp1 % (10 ** 9 + 7), dp2 % (10 ** 9 + 7)

        return dp1 % (10 ** 9 + 7)
