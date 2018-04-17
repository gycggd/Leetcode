class Solution:
    def findTargetSumWays(self, nums, S):
        total = sum(nums)
        if total<S or (total^S)&1: return 0
        target = (S+total)>>1
        cnt = [0]*(target+1)
        cnt[0] = 1
        for n in nums:
            for i in range(target, -1, -1):
                if i-n<0: break
                cnt[i] += cnt[i-n]
        return cnt[target]