class Solution:
    def maxProduct(self, nums):
        def dc(arr, l, r):
            if l==r: return arr[l]
            mid = (l+r)>>1
            return max(dc(arr, l, mid), dc(arr, mid+1, r), merge(arr, l, r, mid))
        
        def merge(arr, l, r, m):
            lmax, lmin = arr[m], arr[m]
            rmax, rmin = 1, 1
            
            i, prod = m-1, arr[m]
            while i>=l:
                prod *= arr[i]
                lmax, lmin = max(prod, lmax), min(prod, lmin)
                if prod==0: break
                i -= 1
            
            j, prod = m+1, 1
            while j<=r:
                prod *= arr[j]
                rmax, rmin = max(prod, rmax), min(prod, rmin)
                if prod==0: break
                j += 1
            return max(lmax*rmax, lmin*rmin)
        
        return dc(nums, 0, len(nums)-1)