class Solution:
    def isInterleave(self, s1, s2, s3):
        l1, l2 = len(s1), len(s2)
        if len(s3)!=l1+l2: return False
        if l1==0 or l2==0: return (l1 and s1==s3) or (l2 and s2==s3) or not s3
        options = {(0, 0)}
        for c in s3:
            new_options = set()
            for (i1, i2) in options:
                if i1<l1 and s1[i1]==c: new_options.add((i1+1, i2))
                if i2<l2 and s2[i2]==c: new_options.add((i1, i2+1))
            if not new_options: return False
            options = new_options
        return True