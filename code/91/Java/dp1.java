class Solution {
    public int numDecodings(String s) {
        if (s==null || s.length()==0) return 0;
        int len = s.length();
        int memo[] = new int[len];
        for (int i=0; i<len; i++) memo[i] = -1;
        return count(s.toCharArray(), 0, memo);
    }
    
    private int count(char[] ca, int i, int[] memo) {
        if (i>ca.length) 
            return 0;
        if (i==ca.length) 
            return 1;
        if (memo[i]==-1) {
            int ret;
            if (ca[i]=='0') 
                ret = 0;
            else if (ca[i]=='1' || (ca[i]=='2' && i+1<ca.length && ca[i+1]<='6')) 
                ret = count(ca, i+1, memo)+count(ca, i+2, memo);
            else 
                ret = count(ca, i+1, memo);
            memo[i] = ret;
        }   
        return memo[i];
    }
    
}