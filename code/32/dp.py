class Solution:
    def longestValidParentheses(self, s):
        length = [0]*len(s)
        for i in range(len(s)):
            if s[i]=='(':
                length[i] = 0
            elif i-1>=0:
                if s[i-1]=='(':
                    length[i] = (length[i-2] if i-2>=0 else 0)+2
                elif i-1-length[i-1]>=0 and s[i-1-length[i-1]]=='(':
                    length[i] = 2+length[i-1]+(length[i-2-length[i-1]] if i-2-length[i-1]>=0 else 0)
        return max(length) if len(s)>0 else 0
