class Solution {
    public int numDecodings(String s) {
        if (s==null || s.length()==0) return 0;
        char[] ca = s.toCharArray();
        int dp[] = new int[s.length()];
        if (ca[0]!='0') dp[0]=1;
        for (int i=1; i<s.length(); i++) {
            if (ca[i]!='0') dp[i] += dp[i-1];
            if (ca[i-1]=='1' || (ca[i-1]=='2' && ca[i]<='6')) dp[i] += (i-2>=0? dp[i-2]: 1);
        }
        return dp[s.length()-1];
    }
}
