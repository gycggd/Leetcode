class Solution:
    def largestSumOfAverages(self, A, K):
        N = len(A)
        ps = [0]*N
        for i in range(N):
            ps[i] = (ps[i-1] if i-1>=0 else 0)+A[i]
        def avg(i, j):
            x = (ps[j]-(ps[i-1] if i-1>=0 else 0))/(j-i+1)
            return x
        dic = {}
        def dp(i, k):
            if k==0: 
                return 0 if i==len(A) else -sys.maxsize
            if i+k>len(A): return -sys.maxsize
            if k==1: return avg(i, len(A)-1)
            if (i, k) not in dic:
                ret = -sys.maxsize
                for j in range(i, len(A)):
                    x = dp(j+1, k-1)
                    ret = max(ret, x+avg(i, j))
                dic[(i, k)] = ret
            return dic[(i, k)]
        return dp(0, K)