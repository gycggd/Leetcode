# author: guoyc
# leetcode url: https://leetcode.com/problems/create-maximum-number/description/

from copy import copy
from collections import defaultdict


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        m = len(nums1)
        n = len(nums2)

        def find_max(nums, p):
            l = len(nums)
            res = []
            s = 0
            for i in reversed(range(p)):
                tmp = 0
                for j in range(s, l - i):
                    if nums[j] > tmp:
                        s = j + 1
                        tmp = nums[j]
                res.append(tmp)
            return res

        def compare(a, b, l):
            for i in range(l):
                if a[i] > b[i]:
                    return 1
                elif a[i] < b[i]:
                    return -1
            return 0

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a + b]

        ans = [0] * k
        for i in range(max(k - n, 0), min(k + 1, m + 1)):
            tmp = merge(find_max(nums1, i), find_max(nums2, k - i))
            if compare(ans, tmp, k) <= 0:
                ans = tmp

        return ans


class Solution2(object):
    def pre_process(self, num):
        l = len(num)
        summary = [[] for _ in range(l)]
        last = [l] * 10
        for i in range(l - 1, -1, -1):
            last[num[i]] = i
            summary[i] = copy(last)
        return summary

    def get_next(self, summary, start, end):
        for i in range(9, -1, -1):
            if summary[start][i] < end:
                return summary[start][i], i

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        summary1 = self.pre_process(nums1)
        summary2 = self.pre_process(nums2)
        candidates = {0: 0}
        max_val = []
        l1 = len(nums1)
        l2 = len(nums2)
        for i in range(k):
            # print(max_val)
            updated_candidates = defaultdict(lambda: (l2, 0))
            round_max = -1
            for x, y in candidates.items():
                remain = max(0, (k - i) - (l2 - y) - 1)
                if l1 - x >= remain and l1 - x > 0:
                    if x + 1 == l1 - remain:
                        pos1, max1 = x, nums1[x]
                    else:
                        pos1, max1 = self.get_next(summary1, x, l1 - remain)
                else:
                    pos1, max1 = l1, -1
                remain = max(0, (k - i) - (l1 - x) - 1)
                if l2 - y >= remain and l2 - y > 0:
                    if y + 1 == l2 - remain:
                        pos2, max2 = y, nums2[y]
                    else:
                        pos2, max2 = self.get_next(summary2, y, l2 - remain)
                else:
                    pos2, max2 = l2, -1
                round_max = max(max1, max2, round_max)
                if max1 == round_max:
                    updated_candidates[pos1 + 1] = (y, max1)
                if max2 == round_max:
                    updated_candidates[x] = (pos2 + 1, max2)
            max_val.append(round_max)
            candidates.clear()
            for l, v in updated_candidates.items():
                if v[1] == round_max:
                    candidates[l] = v[0]
        return max_val
