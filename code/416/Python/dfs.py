class Solution:
    def canPartition(self, nums):
        total=sum(nums)
        if total&1:
            return False
        target = total/2
        
        nums.sort(reverse=True)
        
        def dfs(idx, target):
            if idx==len(nums):
                return target==0
            num=nums[idx]
            if target>num*(len(nums)-idx): return False
            if target>=num and dfs(idx+1,target-num):return True
            if dfs(idx+1,target):return True
            return False
        return dfs(0, target)