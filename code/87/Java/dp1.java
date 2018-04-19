class Solution {
    public boolean isScramble(String s1, String s2) {
        if (s1.length()!=s2.length()) {
            return false;
        }
        if (s1.equals(s2)) {
            return true;
        }
        int counter1[] = new int[26], counter2[]=new int[26];
        for (char c:s1.toCharArray()) {
            counter1[c-'a']++;
        }
        for (char c:s2.toCharArray()) {
            counter2[c-'a']++;
        }
        for (int i=0; i<26; i++) {
            if (counter1[i]!=counter2[i]) {
                return false;
            }
        }
        int N = s1.length();
        int prefixSum1 = 0;
        int prefixSum2 = 0, suffixSum2 = 0;
        for (int i=0; i<N; i++) {
            if (i>0 && prefixSum1==prefixSum2 && isScramble(s1.substring(0, i), s2.substring(0, i)) &&
                isScramble(s1.substring(i), s2.substring(i))) {
                return true;
            }
            if (i>0 && prefixSum1==suffixSum2 && isScramble(s1.substring(0, i), s2.substring(N-i)) &&
                isScramble(s1.substring(i), s2.substring(0, N-i))) {
                return true;
            }
            prefixSum1 += s1.charAt(i);
            prefixSum2 += s2.charAt(i);
            suffixSum2 += s2.charAt(N-1-i);
        }
        return false;
    }
}