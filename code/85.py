# author: guoyc
# leetcode url: https://leetcode.com/problems/maximal-rectangle/description/

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)

        if m == 0:
            return 0

        n = len(matrix[0])

        left = [0] * n
        right = [n] * n
        height = [0] * n

        max_area = 0

        for i in range(m):
            curr_l = 0
            curr_r = n
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], curr_l)
                else:
                    left[j] = 0
                    curr_l = j + 1
            for j in reversed(range(n)):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_r)
                else:
                    right[j] = n
                    curr_r = j

            for j in range(n):
                area = (right[j] - left[j]) * height[j]
                max_area = area if area > max_area else max_area

        return max_area


class Solution2(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        res = 0
        for row in matrix:
            for i in range(len(row)):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(len(row) + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res
