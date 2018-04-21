class Solution {
    public boolean canPartition(int[] nums) {
        // int total = IntStream.of(nums).sum();
        int total = 0;
        for (int n:nums) {
            total += n;
        }
        if ((total&1)==1) {
            return false;
        }
        int target = total>>1;
        Arrays.sort(nums);
        return dfs(nums, nums.length-1, target);
    }
    
    private boolean dfs(int[] nums, int idx, int target) {
        if (idx<0) {
            return target==0;
        }
        if (target==0) {
            return true;
        }
        if (target>nums[idx]*idx) {
            return false;
        }
        if (target>=nums[idx] && dfs(nums, idx-1, target-nums[idx])) {
            return true;
        }
        if (dfs(nums, idx-1, target)) {
            return true;
        }
        return false;
    }
}