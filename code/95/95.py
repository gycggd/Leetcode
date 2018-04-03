# author: guoyc
# leetcode url: https://leetcode.com/problems/unique-binary-search-trees-ii/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None  # Definition for a binary tree node.


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generate(1, n)

    def generate(self, s, e):
        if s > e:
            return [None]
        result = []
        for i in range(s, e + 1):
            left = self.generate(s, i - 1)
            right = self.generate(i + 1, e)
            for ln in left:
                for rn in right:
                    md = TreeNode(i)
                    md.left = ln
                    md.right = rn
                    result.append(md)
        return result


class Solution2(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        result = [[] for _ in range(n + 1)]

        if n == 0:
            return result[0]

        result[0] = [None]

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                for ln in result[j - 1]:
                    for rn in self.increment(result[i - j], j):
                        md = TreeNode(j)
                        md.left = ln
                        md.right = rn
                        result[i].append(md)

        return result[n]

    def increment(self, result, i):
        return [self.clone(n, i) for n in result]

    def clone(self, node, i):
        if node == None:
            return None
        copy = TreeNode(node.val + i)
        copy.left = self.clone(node.left, i)
        copy.right = self.clone(node.right, i)
        return copy
