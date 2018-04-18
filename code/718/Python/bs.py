class Solution:
    def findLength(self, A, B):
        
        def check(length):
            seen = {A[i:i+length]
                    for i in range(len(A) - length + 1)}
            return any(B[j:j+length] in seen
                       for j in range(len(B) - length + 1))

        A = ''.join(map(chr, A))
        B = ''.join(map(chr, B))
        lo, hi = 0, min(len(A), len(B)) + 1
        while lo+1 < hi:
            mi = (lo + hi) // 2
            if check(mi):
                lo = mi
            else:
                hi = mi
        return lo