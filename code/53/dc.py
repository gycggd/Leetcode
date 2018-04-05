class Solution:
    def maxSubArray(self, nums):
        
        def dc(nums, l, r):
            if l>=r: return 0 if l>r else nums[l]
            mid = (l+r)>>1
            return max(dc(nums, l, mid), dc(nums, mid+1, r), cross(nums, mid, l, r))

        def cross(nums, mid, l,r):
            left_sum, left_max = nums[mid], nums[mid]
            for _ in range(mid-1, l-1, -1):
                left_sum += nums[_]
                left_max = max(left_sum, left_max)
            right_sum, right_max = 0, 0
            for _ in range(mid+1, r+1):
                right_sum += nums[_]
                right_max = max(right_sum, right_max)
            return left_max+right_max
        return dc(nums, 0, len(nums)-1)
                