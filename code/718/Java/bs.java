class Solution {
    public int findLength(int[] A, int[] B) {
        
        // String strA = Arrays.stream(A).collect(StringBuilder::new, 
        // StringBuilder::appendCodePoint, StringBuilder::append).toString();
        // String strB = Arrays.stream(B).collect(StringBuilder::new, 
        // StringBuilder::appendCodePoint, StringBuilder::append).toString();
        
        StringBuilder sbA = new StringBuilder(), sbB = new StringBuilder();
        for (int i:A)
            sbA.append((char)i);
        for (int i:B)
            sbB.append((char)i);
        String strA=sbA.toString(), strB=sbB.toString();
        
        int left=0, right=Math.min(A.length, B.length)+1;
        while (left+1<right) {
            int mid = (left+right)>>1;
            if (check(strA, strB, mid)) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return left;
    }
    
    private boolean check(String strA, String strB, int len) {
        Set<String> set = new HashSet<>();
        for (int i=0; i<strA.length()-len+1; i++) {
            set.add(strA.substring(i, i+len));
        }
        
        for (int i=0; i<strB.length()-len+1; i++) {
            if (set.contains(strB.substring(i, i+len))) {
                return true;
            }
        }
        return false;
        
    }
}