# author: guoyc
# leetcode url: https://leetcode.com/problems/word-break-ii/description/

class Solution(object):
    def wordBreak(self, s, wordDict):
        l = len(s)

        mem = {l: ['']}

        def cut(i):
            if i not in mem:
                mem[i] = [s[i:j + 1] + (t and ' ' + t)
                          for j in range(i, l) if s[i:j + 1] in wordDict
                          for t in cut(j + 1)]
            return mem[i]

        return cut(0)
