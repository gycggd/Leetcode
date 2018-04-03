class Solution:
    def longestValidParentheses(self, s):
        ret = 0
        l, r = 0, 0
        for c in s:
            if c=='(':
                l += 1
            else:
                r += 1
            if l==r:
                ret = max(ret, l+r)
            elif l<r:
                l, r = 0, 0
        l, r = 0, 0
        for c in s[::-1]:
            if c=='(':
                l += 1
            else:
                r += 1
            if l==r:
                ret = max(ret, l+r)
            elif l>r:
                l, r = 0, 0
        return ret
