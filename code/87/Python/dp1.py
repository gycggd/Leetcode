class Solution:
    def isScramble(self, s1, s2):
        if len(s1)!=len(s2): return False
        def check(S1, S2):
            if S1==S2: return True
            if sorted(S1)!=sorted(S2): return False
            N = len(S1)
            prefixSum1 = 0
            prefixSum2, suffixSum2 = 0, 0
            for i in range(N):
                if i>0 and prefixSum1==prefixSum2 and check(S1[:i], S2[:i]) and check(S1[i:], S2[i:]): return True
                if i>0 and prefixSum1==suffixSum2 and check(S1[:i], S2[N-i:]) and check(S1[i:], S2[:N-i]): return True
            return False
        return check(s1, s2)