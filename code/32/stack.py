class Solution:
    def longestValidParentheses(self, s):
        st = []
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                if st:
                    if s[st[-1]]=='(':
                        st.pop(-1)
                    else:
                        st.append(i)
                else:
        if not st:
            return len(s)
        start, end = 0, len(s)
        ret = 0
        while st:
            start = st.pop(-1)
            ret = max(ret, end-start-1)
            end = start
        ret = max(ret, end)
        return ret
