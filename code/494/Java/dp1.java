class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        return dp(nums, nums.length-1, S, new HashMap<>());
    }
    public int dp(int[] nums, int i, int target, Map<String, Integer> memo) {
        if (i==-1) {
            return target==0?1:0;
        }
        String key = String.valueOf(i)+','+String.valueOf(target);
        if (!memo.containsKey(key)) {
            memo.put(key, dp(nums, i-1, target+nums[i], memo)+dp(nums, i-1, target-nums[i], memo));
        }
        return memo.get(key);
    }
}