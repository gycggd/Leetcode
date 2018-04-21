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
        boolean dp[] = new boolean[target+1];
        dp[0] = true;
        for (int n:nums) {
            for (int i=target; i>=n; i--) {
                dp[i] |= dp[i-n];
            }
        }
        return dp[target];
    }
}