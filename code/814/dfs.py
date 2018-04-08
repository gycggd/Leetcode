class Solution:
    def pruneTree(self, root):
        def dfs(node):
            if not node: return False
            l, r = dfs(node.left), dfs(node.right)
            if not l: node.left = None
            if not r: node.right = None
            return (node.val==1) or l or r
        x = dfs(root)
        if not x:
            return None
        return root