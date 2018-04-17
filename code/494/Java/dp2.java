class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        int total = Arrays.stream(nums).sum();
        if (total<S || ((total^S)&1)==1) {
            return 0;
        }
        int plus = (total+S)>>1;
        int cnt[] = new int[plus+1];
        cnt[0] = 1;
        for (int n:nums) {
            for (int i=plus; i>=n; i--) {
                cnt[i] += cnt[i-n];
            }
        }
        return cnt[plus];
    }
}